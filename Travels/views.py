from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Travel, TravelImage, MemoryImage

@login_required
def travel_list(request):
    travels = Travel.objects.filter(user=request.user)
    city = request.GET.get('city')
    state = request.GET.get('state')
    district = request.GET.get('district')
    country = request.GET.get('country')

    if city:
        travels = travels.filter(city__icontains=city)
    if state:
        travels = travels.filter(state__icontains=state)
    if district:
        travels = travels.filter(district__icontains=district)
    if country:
        travels = travels.filter(country__icontains=country)

    travels = travels.order_by('-created_at')
    return render(request, 'travels/travel_list.html', {'travels': travels, 'city': city, 'state': state, 'district': district, 'country': country})

@login_required
def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk, user=request.user)
    images = travel.images.all()
    return render(request, 'travels/travel_detail.html', {'travel': travel, 'images': images})

@login_required
def travel_create(request):
    if request.method == 'POST':
        place_name = request.POST.get('place_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        district = request.POST.get('district')
        additional_notes = request.POST.get('additional_notes')
        budget = request.POST.get('budget')
        travel_route = request.POST.get('travel_route')
        travel_completed = request.POST.get('travel_completed') == 'True'

        travel = Travel.objects.create(
            user=request.user,
            place_name=place_name,
            city=city,
            state=state,
            country=country,
            district=district,
            additional_notes=additional_notes,
            budget=budget if budget else None,
            travel_route=travel_route,
            travel_completed=travel_completed
        )

        images = request.FILES.getlist('images')
        for image in images[:5]:
            TravelImage.objects.create(travel=travel, image=image)

        return redirect('travel_list')
    else:
        return render(request, 'travels/travel_form.html')

@login_required
def travel_edit(request, pk):
    travel = get_object_or_404(Travel, pk=pk, user=request.user)
    if request.method == 'POST':
        travel.place_name = request.POST.get('place_name')
        travel.city = request.POST.get('city')
        travel.state = request.POST.get('state')
        travel.country = request.POST.get('country')
        travel.district = request.POST.get('district')
        travel.additional_notes = request.POST.get('additional_notes')
        budget = request.POST.get('budget')
        travel.budget = budget if budget else None
        travel.travel_route = request.POST.get('travel_route')
        travel.travel_completed = request.POST.get('travel_completed') == 'True'
        travel.save()

        images = request.FILES.getlist('images')
        for image in images[:5]:
            TravelImage.objects.create(travel=travel, image=image)

        return redirect('travel_list')
    else:
        context = {
            'place_name': travel.place_name,
            'city': travel.city,
            'state': travel.state,
            'country': travel.country,
            'district': travel.district,
            'additional_notes': travel.additional_notes,
            'budget': travel.budget,
            'travel_route': travel.travel_route,
            'travel_completed': travel.travel_completed,
        }
        return render(request, 'travels/travel_form.html', context)

@login_required
def mark_travel_completed(request, pk):
    travel = get_object_or_404(Travel, pk=pk, user=request.user)
    if request.method == 'POST':
        travel.travel_completed = True
        travel.save()
    return redirect('travel_detail', pk=pk)

@login_required
def completed_travel_list(request):
    travels = Travel.objects.filter(user=request.user, travel_completed=True).order_by('-updated_at')
    return render(request, 'travels/completed_travel_list.html', {'travels': travels})

@login_required
def upload_memories(request, pk):
    travel = get_object_or_404(Travel, pk=pk, user=request.user)
    if request.method == 'POST':
        images = request.FILES.getlist('memories')
        if len(images) < 1:
            error = "Please upload at least 1 image."
            return render(request, 'travels/upload_memories.html', {'travel': travel, 'error': error})
        if len(images) > 20:
            error = "You can upload a maximum of 20 images."
            return render(request, 'travels/upload_memories.html', {'travel': travel, 'error': error})
        for image in images:
            MemoryImage.objects.create(user=request.user, travel=travel, image=image)
        return redirect('show_memories', pk=pk)
    return render(request, 'travels/upload_memories.html', {'travel': travel})

@login_required
def show_memories(request, pk):
    travel = get_object_or_404(Travel, pk=pk, user=request.user)
    images = travel.memory_images.all()
    return render(request, 'travels/show_memories.html', {'travel': travel, 'images': images})
