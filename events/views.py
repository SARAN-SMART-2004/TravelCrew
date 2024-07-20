from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
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

def event_list(request):
    events = Event.objects.all()
    context = get_user_context(request)
    context.update({
        'events': events,  # Pass unique users to the context
    })
    return render(request, 'event_list.html', context)

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    context = get_user_context(request)
    context.update({
        'form': form,
    
    })
    return render(request, 'event_form.html', context)
