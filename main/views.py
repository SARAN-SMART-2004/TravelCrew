
from users.models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TravelPlan
from django.db.models import Q
from users.models import Feedback
from users.forms import FeedbackForm
from django.utils import timezone
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TravelPlanForm,TripMessage
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from users.forms import Feedback
from users.models import Feedback
from django.shortcuts import render, get_object_or_404, redirect

def get_user_context(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        context.update({
            'current_user': current_user,
            'username': current_user.username,
            'email': current_user.email,
            'description': current_user.description,
            'phone_number': current_user.phone_number,
            'image': current_user.image,
        })
    return context

def homepage(request):
    context = get_user_context(request)
    return render(request, 'main/design/header.html', context)



def dashboard(request):
    context = get_user_context(request)
    return render(request, 'main/design/boxindex.html', context)

def search(request):
    context = get_user_context(request)
    return render(request, 'main/includes/search.html', context)


def people(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/userprofile/people.html', context)




def user_profile(request, pk):
    context = get_user_context(request)
    user = get_object_or_404(get_user_model(), id=pk)
    feedbacks = user.feedbacks.all()  # Get feedback related to the user

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_instance = form.save(commit=False)
            feedback_instance.user = user  # Link feedback to the user
            feedback_instance.save()
            messages.success(request, "Your feedback has been Submitted. You information will be  <b>usefull </b> for others.")
            return redirect('user_profile', pk=pk)  # Redirect back to the profile page
    else:
        form = FeedbackForm()

    context.update({
        'user': user,
        'feedbacks': feedbacks,
        'form': form
    })
    
    return render(request, 'main/userprofile/user_profile.html', context)




# def user_profile(request, pk):
#     context = get_user_context(request)
#     user = get_object_or_404(CustomUser, pk=pk)
#     context.update({'user': user})
    
#     return render(request, 'main/userprofile/user_profile.html', context)


@login_required
def submit_travel_plan(request):
    context = get_user_context(request)
    if request.method == 'POST':
        source_place = request.POST.get('source_place')
        destination_place = request.POST.get('destination_place')
        date = request.POST.get('date')
        leaving_time = request.POST.get('leaving_time')
        waiting_time = request.POST.get('waiting_time')
        message = request.POST.get('message')

        TravelPlan.objects.create(
            source_place=source_place,
            destination_place=destination_place,
            date=date,
            leaving_time=leaving_time,
            waiting_time=waiting_time,
            message=message,
            organizer=request.user,
            created_at=timezone.now()
        )
        messages.success(request, f"You have successfully created the post !!!")
        return redirect('homepage')  # Redirect to a success page or another page of your choice

    return render(request, 'main/posts/createpost.html',context)


@login_required
def edit_all_travel_plans(request):
    context = get_user_context(request)
    current_user = request.user
    travel_plans = TravelPlan.objects.filter(organizer=current_user)
    today = timezone.now().date()
    context.update({
        'travel_plans': travel_plans,
        'today': today
    })
    return render(request, 'main/posts/editpost.html', context)


@login_required
def edit_travel_plan(request, pk):
    context = get_user_context(request)
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    if request.method == 'POST':
        form = TravelPlanForm(request.POST, instance=travel_plan)
        if form.is_valid():
            form.save()
            messages.success(request, f"You have successfully edited the post !!!")
            return redirect('all_travel_plans')
    else:
        form = TravelPlanForm(instance=travel_plan)
    context.update({'form': form})
    return render(request, 'main/posts/edit.html', context)

@login_required
def past_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date__lt=current_date)
    past_travel_plans = past_travel_plans.order_by('-id')
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/posts/past.html',context)



@login_required
def upcoming_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date__gt=current_date)
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/posts/upcoming.html', context)

def ongoing_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date=current_date)
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/posts/ongoing.html', context)


@login_required
def user_past_history(request):
    context = get_user_context(request)
    current_user = request.user
    
    # Fetching travel plans organized by the user
    organized_travel_plans = TravelPlan.objects.filter(organizer=current_user)
    
    # Fetching travel plans where the user is a member
    member_travel_plans = TravelPlan.objects.filter(members=current_user)

    # Combining both querysets
    user_travel_plans = organized_travel_plans | member_travel_plans
    
    ongoing_trips = []
    upcoming_trips = []
    completed_trips = []

    current_date = timezone.now().date()
    for plan in user_travel_plans:
        if plan.date < current_date:
            completed_trips.append(plan)
        elif plan.date == current_date:
            ongoing_trips.append(plan)
        else:
            upcoming_trips.append(plan)

    context.update({
        'ongoing_trips': ongoing_trips,
        'upcoming_trips': upcoming_trips,
        'completed_trips': completed_trips,
    })
    return render(request, 'main/userposts/userpast.html', context)



@login_required
def user_upcoming_history(request):
    context = get_user_context(request)
    current_user = request.user
    
    # Fetching travel plans organized by the user
    organized_travel_plans = TravelPlan.objects.filter(organizer=current_user)
    
    # Fetching travel plans where the user is a member
    member_travel_plans = TravelPlan.objects.filter(members=current_user)

    # Combining both querysets
    user_travel_plans = organized_travel_plans | member_travel_plans
    
    ongoing_trips = []
    upcoming_trips = []
    completed_trips = []

    current_date = timezone.now().date()
    for plan in user_travel_plans:
        if plan.date < current_date:
            completed_trips.append(plan)
        elif plan.date == current_date:
            ongoing_trips.append(plan)
        else:
            upcoming_trips.append(plan)

    context.update({
        'ongoing_trips': ongoing_trips,
        'upcoming_trips': upcoming_trips,
        'completed_trips': completed_trips,
    })
    return render(request, 'main/userposts/userupcoming.html', context)

@login_required
def user_ongoing_history(request):
    context = get_user_context(request)
    current_user = request.user
    
    # Fetching travel plans organized by the user
    organized_travel_plans = TravelPlan.objects.filter(organizer=current_user)
    
    # Fetching travel plans where the user is a member
    member_travel_plans = TravelPlan.objects.filter(members=current_user)

    # Combining both querysets
    user_travel_plans = organized_travel_plans | member_travel_plans
    
    ongoing_trips = []
    upcoming_trips = []
    completed_trips = []

    current_date = timezone.now().date()
    for plan in user_travel_plans:
        if plan.date < current_date:
            completed_trips.append(plan)
        elif plan.date == current_date:
            ongoing_trips.append(plan)
        else:
            upcoming_trips.append(plan)

    context.update({
        'ongoing_trips': ongoing_trips,
        'upcoming_trips': upcoming_trips,
        'completed_trips': completed_trips,
    })
    return render(request, 'main/userposts/ongoing.html', context)



def travel_plan_details(request, pk):
    context = get_user_context(request)
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    now = timezone.now()
    # Check if the trip date is in the past
    current_date = timezone.now().date()
    is_past_trip = travel_plan.date < current_date

    context.update({
        'travel_plan': travel_plan,
        'is_past_trip': is_past_trip,
        'now': now,
    })
    return render(request, 'main/posts/travel_plan_details.html', context)



from django.views.generic.detail import DetailView
class TravelPlanDetailView(DetailView):
    model = TravelPlan
    template_name = 'main/travel_plan_detail.html'
    context_object_name = 'travel_plan'


@login_required
def accept_trip(request, pk):
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    user = request.user

    if 'accept' in request.POST:

        travel_plan.members.add(user)
         # Create message for acceptance

        TripMessage.objects.create(
            sender=user,
            recipient=travel_plan.organizer,
            content=f'{user.username} has accepted the trip from {travel_plan.source_place} to {travel_plan.destination_place}.',
        )

        message = render_to_string('main/mail/template_trip_accepted.html', {'user': user})
        send_mail(
            'Trip Accepted',
            message,
            'smartsaran3031@gmail.com',  # Replace with your email or settings.DEFAULT_FROM_EMAIL
            [travel_plan.organizer.email],
            fail_silently=False,
        )
        messages.success(request, f"You have successfully Accepted the Trip !!!")
    elif 'cancel' in request.POST:
        travel_plan.members.remove(user)
         # Create message for cancellation
        message = render_to_string('main/mail/template_trip_canceled.html', {'user': user})
        TripMessage.objects.create(
            sender=user,
            recipient=travel_plan.organizer,
            content=f"{user.username} has canceled their trip membership for '{travel_plan.source_place} to {travel_plan.destination_place}' scheduled on {travel_plan.date}.",
        )
        send_mail(
            'Trip Canceled',
            message,
            'smartsaran3031@gmail.com',  # Replace with your email or settings.DEFAULT_FROM_EMAIL
            [travel_plan.organizer.email],
            fail_silently=False,
        )
        messages.error(request, "You Cancelled the accepted trip.")

    return redirect(reverse('travel_plan_detail', args=[pk]))


@login_required
def all_travel_plans(request):
    context = get_user_context(request)

    # Get all travel plans
    travel_plans = TravelPlan.objects.all()
    travel_plans = travel_plans.order_by('-id')
    current_date = timezone.now().date()

    # Implement search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        travel_plans = travel_plans.filter(
            Q(organizer__username__icontains=search_query) |
            Q(source_place__icontains=search_query) |
            Q(destination_place__icontains=search_query) |
            Q(date__icontains=search_query) |
            Q(leaving_time__icontains=search_query)
        )

    # Update status for filtered travel plans
    for plan in travel_plans:
        if plan.date < current_date:
            plan.status = 'Completed'
        elif plan.date == current_date:
            plan.status = 'Ongoing'
        else:
            plan.status = 'Upcoming'

    context.update({'travel_plans': travel_plans, 'search_query': search_query})
    return render(request, 'main/posts/posts.html', context)



@login_required
def search_travel_plans(request):
    search_query = request.GET.get('search', '')
    travel_plans = TravelPlan.objects.all()

    if search_query:
        travel_plans = travel_plans.filter(
            Q(organizer__username__icontains=search_query) |
            Q(source_place__icontains=search_query) |
            Q(destination_place__icontains=search_query) |
            Q(date__icontains=search_query) |
            Q(leaving_time__icontains=search_query)
        )

    # Update status for each travel plan
    current_date = timezone.now().date()
    for plan in travel_plans:
        if plan.date < current_date:
            plan.status = 'Completed'
        elif plan.date == current_date:
            plan.status = 'Ongoing'
        else:
            plan.status = 'Upcoming'

    context = {
        'travel_plans': travel_plans,
        'search_query': search_query,
    }
    return render(request, 'main/posts/posts.html', context)
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TravelPlan, JoinRequest

@login_required
def travel_plan_details(request, pk):
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    is_member = request.user in travel_plan.members.all()
    # Determine if the travel plan is upcoming
    current_date = timezone.now().date()
    is_upcoming_trip = travel_plan.date > current_date
    
    join_request = JoinRequest.objects.filter(user=request.user, travel_plan=travel_plan, is_accepted=False).first()
    context = get_user_context(request)
    context.update({
        'travel_plan': travel_plan,
        'is_member': is_member,
        'join_request': join_request,
        'is_upcoming_trip': is_upcoming_trip,
        
    })
    if request.method == "POST":
        if 'join' in request.POST:
            if not join_request:
                join_request = JoinRequest.objects.create(user=request.user, travel_plan=travel_plan)
                send_mail(
                    'Join Request',
                    f'{request.user.username} wants to join your travel plan. Could you accept it?\n '
                    'If you are interested in traveling with the user, then log in to the TravelCrew app and accept the request.\n\n'
                    'Thank you,\n'
                    'Team TravelCrew',
                    settings.EMAIL_HOST_USER,
                    [travel_plan.organizer.email],
                )
                messages.success(request, "Join request sent.")
                user=request.user
                # When a user requests to join a trip
                TripMessage.objects.create(
                sender=user,  # the user who is sending the request
                recipient=travel_plan.organizer,  # the organizer of the trip
                content=f"{user.username} wants to join the trip from {travel_plan.source_place} to {travel_plan.destination_place}."
                )
        elif 'accept' in request.POST:
            join_request_id = request.POST.get('accept')
            join_request = get_object_or_404(JoinRequest, id=join_request_id)
            join_request.is_accepted = True
            join_request.save()
            travel_plan.members.add(join_request.user)
            
            send_mail(
                'Join Request Accepted',
                f'Your request to join the travel plan has been accepted.\n'
                'I hope this message finds you well. TravelCrew team pleased to inform you that trip organizer accept your invitation to join the upcoming trip.\n'
                'Thank you ,\n'
                'Team TravelCrew',
                settings.EMAIL_HOST_USER,
                [join_request.user.email],
            )
            messages.success(request, "Member accepted.")
            user=request.user
            # When the organizer accepts a join request
            TripMessage.objects.create(
            sender=travel_plan.organizer,  # the organizer sending the message
            recipient=user,  # the user who requested to join
            content=f"Organizer has accepted the trip from {travel_plan.source_place} to {travel_plan.destination_place}."
            )
        elif 'cancel' in request.POST:
            travel_plan.members.remove(request.user)
            send_mail(
                'Member trip Cancellation',
                f'{request.user.username} has canceled their Trip membership.\n'
                'we hope this message finds you well. We regret to inform you that due to unforeseen personal circumstances of the member,\n'
                ' Member has cancel the  acceptance of the trip.'
                'We apologize for any inconvenience this may cause and kindly request your understanding regarding this matter.'
                'Thank you for your consideration.\n'
                'Thank you ,\n'
                'Team TravelCrew',
                settings.EMAIL_HOST_USER,
                [travel_plan.organizer.email],
            )
            messages.success(request, "Membership canceled.")
            user=request.user
            TripMessage.objects.create(
            sender=user,
            recipient=travel_plan.organizer,
            content=f'{user.username} has cancelled the trip from {travel_plan.source_place} to {travel_plan.destination_place}.',)
        return redirect('travel_plan_details', pk=travel_plan.pk)

    
    context.update({'travel_plan': travel_plan})
    context.update({'is_member': is_member})
    context.update({'join_request': join_request})
    
    return render(request, 'main/posts/travel_plan_details.html', context)
 # Adjust based on your actual model structure

  # Updated import to reflect the new class name
from .models import TripMessage  # Update this based on your actual model name


@login_required
def user_messages(request):
    received_messages = TripMessage.objects.filter(recipient=request.user)
    
    organizer_messages = []  # For join requests
    member_messages = []  # For acceptance notifications
    cancellation_messages = []  # For cancellation notifications

    for message in received_messages:
        if "wants to join the trip" in message.content:
            organizer_messages.append(message)
        elif "has accepted the trip" in message.content:
            member_messages.append(message)
        elif "has canceled the trip" in message.content:
            cancellation_messages.append(message)

    context = {
        'member_messages': member_messages,
        'organizer_messages': organizer_messages,
        'cancellation_messages': cancellation_messages,
    }
    return render(request, 'main/message.html', context)
from .models import Request, TravelPlan





@login_required
def requests(request):
    context = get_user_context(request)
    travel_plans = TravelPlan.objects.all()
    sent_requests = JoinRequest.objects.filter(user=request.user)  # Join requests sent by the user
    sent_requests = sent_requests.order_by('-id')
    received_requests = JoinRequest.objects.filter(travel_plan__organizer=request.user, is_accepted=False)  # Join requests received by the user
    received_requests = received_requests.order_by('-id')
    context.update ({
        'sent_requests': sent_requests,
        'received_requests': received_requests,
        'travel_plans':travel_plans,
    })
    
    return render(request, 'main/posts/requests.html', context)





from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import TravelPlan  # Ensure you have this model defined

def filter_travel_plans(request):
    context = get_user_context(request)
    if request.method == 'POST':
        source_place = request.POST.get('source_place', '').lower()
        destination_place = request.POST.get('destination_place', '').lower()
        travel_date = request.POST.get('travel_date', '')
        
        # Build the query dynamically
        filters = Q()
        
        if source_place:
            filters &= Q(source_place__iexact=source_place)
        
        if destination_place:
            filters &= Q(destination_place__iexact=destination_place)
        
        if travel_date:
            filters &= Q(date=travel_date)  # Assuming date comparison is exact
        current_date = timezone.now().date()
        # Execute the query with the built filters
        travel_plans = TravelPlan.objects.filter(filters)
        travel_plans = travel_plans.order_by('-id')
        for plan in travel_plans:
            if plan.date < current_date:
                plan.status = 'Completed'
            elif plan.date == current_date:
                plan.status = 'Ongoing'
            else:
                plan.status = 'Upcoming'

        # Context to pass to the template
        context.update({ 
            'source_place': source_place,
            'destination_place': destination_place,
            'travel_date': travel_date,
            'travel_plans': travel_plans,  # Pass filtered plans
        })
        return render(request, 'main/filtered_results.html', context)

    return render(request, 'main/includes/search.html')



