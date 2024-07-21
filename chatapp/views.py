from django.shortcuts import render, get_object_or_404
from .models import Room, Message

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


def rooms(request):
    rooms = Room.objects.all()
    context = get_user_context(request)
    context.update({
        'rooms': rooms,  # Pass unique users to the context
    })
    return render(request, "rooms.html", context)

def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)
    context = get_user_context(request)
    context.update({
        'room_name': room.name,
        "slug": slug, 
        'messages': messages  # Pass unique users to the context
    })
    
    return render(request, "room.html", context)
