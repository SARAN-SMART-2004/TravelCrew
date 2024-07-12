
from users.models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TravelPlan
from django.db.models import Q

from django.utils import timezone
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TravelPlanForm

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
    return render(request, 'main/header.html', context)



def dashboard(request):
    context = get_user_context(request)
    return render(request, 'main/boxindex.html', context)

def people(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/people.html', context)
def user_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'main/user_profile.html', context)


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

    return render(request, 'main/createpost.html',context)


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
    return render(request, 'main/editpost.html', context)


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
    return render(request, 'main/edit.html', context)

@login_required
def past_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date__lt=current_date)
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/past.html',context)



@login_required
def upcoming_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date__gt=current_date)
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/upcoming.html', context)

def ongoing_trips(request):
    context = get_user_context(request)
    current_date = timezone.now().date()
    past_travel_plans = TravelPlan.objects.filter(date=current_date)
    context.update({'past_travel_plans': past_travel_plans})
    return render(request, 'main/ongoing.html', context)


@login_required
def user_post_history(request):
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
    return render(request, 'main/poststatus.html', context)
# @login_required
# def all_travel_plans(request):
#     context = get_user_context(request)

#     travel_plans = TravelPlan.objects.all()
#     current_date = timezone.now().date()
#     for plan in travel_plans:
#         if plan.date < current_date:
#             plan.status = 'Completed'
#         elif plan.date == current_date:
#             plan.status = 'Ongoing'
#         else:
#             plan.status = 'Upcoming'

#     context.update({'travel_plans': travel_plans})
#     return render(request, 'main/posts.html', context)


def travel_plan_details(request, pk):
    context = get_user_context(request)
    travel_plan = get_object_or_404(TravelPlan, pk=pk)

    # Check if the trip date is in the past
    current_date = timezone.now().date()
    is_past_trip = travel_plan.date < current_date

    context.update({
        'travel_plan': travel_plan,
        'is_past_trip': is_past_trip,
    })
    return render(request, 'main/travel_plan_details.html', context)



@login_required
def accept_trip(request, trip_id):
    travel_plan = get_object_or_404(TravelPlan, id=trip_id)
    user = request.user

    if user != travel_plan.organizer:
        travel_plan.members.add(user)
        travel_plan.save()

        send_mail(
            'Trip Accepted',
            f'{user.username} has accepted your trip',
            'from@example.com',  # Replace with your email or settings.DEFAULT_FROM_EMAIL
            [travel_plan.organizer.email],
            fail_silently=False,
        )
        messages.success(request, "You have successfully accepted the trip.")
    else:
        messages.error(request, "You cannot accept your own trip.")

    return HttpResponseRedirect(reverse('travel_plan_detail', args=[trip_id]))
# views.py


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
        message = render_to_string('main/template_trip_accepted.html', {'user': user})
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
        message = render_to_string('main/template_trip_canceled.html', {'user': user})
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
    return render(request, 'main/posts.html', context)



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
    return render(request, 'main/posts.html', context)