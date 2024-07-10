from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# from users.models import SubscribedUsers
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from users.models import CustomUser


# from .models import Article, ArticleSeries
from .decorators import user_is_superuser
# from .forms import NewsletterForm, SeriesCreateForm, ArticleCreateForm, SeriesUpdateForm, ArticleUpdateForm#, NewsletterForm
# from users.models import SubscribedUsers

import os
from uuid import uuid4

from django.shortcuts import render

def homepage(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch all details of the authenticated user
        current_user = request.user
        username = current_user.username
        email = current_user.email
        description = current_user.description
        phone_number = current_user.phone_number
        image=current_user.image
        
        
        context = {
            'current_user': current_user,
            'username': username,
            'email': email,
            'description': description,
            'phone_number': phone_number,
            'image':image,
            
            # Add more data as needed
        }
    else:
        context = {}
    
    return render(request, 'main/header.html', context)



#  matching_series = ArticleSeries.objects.all()
    
#     return render(
#         request=request,
#         template_name='main/home.html',
#         context={
#             "objects": matching_series,
#             "type": "series"
#             }
#         )





def editpost(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch all details of the authenticated user
        current_user = request.user
        username = current_user.username
        email = current_user.email
        description = current_user.description
        phone_number = current_user.phone_number
        image=current_user.image
        
        
        context = {
            'current_user': current_user,
            'username': username,
            'email': email,
            'description': description,
            'phone_number': phone_number,
            'image':image,
            
            # Add more data as needed
        }
    else:
        context = {}
    return render(request,'main/editpost.html',context)
def createpost(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch all details of the authenticated user
        current_user = request.user
        username = current_user.username
        email = current_user.email
        description = current_user.description
        phone_number = current_user.phone_number
        image=current_user.image
        
        
        context = {
            'current_user': current_user,
            'username': username,
            'email': email,
            'description': description,
            'phone_number': phone_number,
            'image':image,
            
            # Add more data as needed
        }
    else:
        context = {}
    return render(request,'main/createpost.html',context)
def poststatus(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch all details of the authenticated user
        current_user = request.user
        username = current_user.username
        email = current_user.email
        description = current_user.description
        phone_number = current_user.phone_number
        image=current_user.image
        
        
        context = {
            'current_user': current_user,
            'username': username,
            'email': email,
            'description': description,
            'phone_number': phone_number,
            'image':image,
            
            # Add more data as needed
        }
    else:
        context = {}
    return render(request,'main/poststatus.html',context)


def dashboard(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch all details of the authenticated user
        current_user = request.user
        username = current_user.username
        email = current_user.email
        description = current_user.description
        phone_number = current_user.phone_number
        image=current_user.image
        
        
        context = {
            'current_user': current_user,
            'username': username,
            'email': email,
            'description': description,
            'phone_number': phone_number,
            'image':image,
            
            # Add more data as needed
        }
    else:
        context = {}
    return render(request,'main/boxindex.html',context)
from django.shortcuts import render
from users.models import CustomUser

def people(request):
    context = {}

    if request.user.is_authenticated:
        current_user = request.user
        context['current_user'] = current_user
        context['username'] = current_user.username
        context['email'] = current_user.email
        context['description'] = current_user.description
        context['phone_number'] = current_user.phone_number
        context['image'] = current_user.image

    users = CustomUser.objects.all()
    context['users'] = users

    return render(request, 'main/people.html', context)
def edit(request):
    return render(request, 'main/edit.html')

