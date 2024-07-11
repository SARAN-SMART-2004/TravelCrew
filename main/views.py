from django.shortcuts import render
from users.models import CustomUser

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

def editpost(request):
    context = get_user_context(request)
    return render(request, 'main/editpost.html', context)

def createpost(request):
    context = get_user_context(request)
    return render(request, 'main/createpost.html', context)

def poststatus(request):
    context = get_user_context(request)
    return render(request, 'main/poststatus.html', context)

def dashboard(request):
    context = get_user_context(request)
    return render(request, 'main/boxindex.html', context)

def people(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/people.html', context)

def edit(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/edit.html', context)

def upcoming_trip(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/upcoming.html', context)

def past_trip(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/past.html', context)

def posts(request):
    context = get_user_context(request)
    context['users'] = CustomUser.objects.all()
    return render(request, 'main/posts.html', context)
from django.urls import resolve

