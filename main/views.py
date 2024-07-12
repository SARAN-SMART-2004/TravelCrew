
from users.models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TravelPlan
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required

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
    context.update({'travel_plans': travel_plans})
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
    user_travel_plans = TravelPlan.objects.filter(organizer=current_user)
    
    current_date = timezone.now().date()
    for plan in user_travel_plans:
        if plan.date < current_date:
            plan.status = 'Completed'
        elif plan.date == current_date:
            plan.status = 'Ongoing'
        else:
            plan.status = 'Upcoming'
    context.update({'user_travel_plans': user_travel_plans})
    return render(request, 'main/poststatus.html', context)
@login_required
def all_travel_plans(request):
    context = get_user_context(request)

    travel_plans = TravelPlan.objects.all()
    current_date = timezone.now().date()
    for plan in travel_plans:
        if plan.date < current_date:
            plan.status = 'Completed'
        elif plan.date == current_date:
            plan.status = 'Ongoing'
        else:
            plan.status = 'Upcoming'

    context.update({'travel_plans': travel_plans})
    return render(request, 'main/posts.html', context)
@login_required
def travel_plan_details(request, pk):
    context = get_user_context(request)
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    context.update({'travel_plan': travel_plan})
    return render(request, 'main/travel_plan_details.html', context)
