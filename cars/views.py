from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars, Color, Body, CarImg
from accounts.models import User
from django.contrib.auth.decorators import login_required

def car_list(request):
    cars = Cars.objects.all()
    context = {
        "cars" : cars,
    }
    return render(request, "cars/car_list.html", context)
    
    
    
    
@login_required
def add_car(request):
    context = {
        "colors": Color.choices,
        "body_conditions": Body.choices,
    }
    if request.method == "POST":
        car = Cars(
            owner=request.user,
            brand=request.POST.get("brand"),
            system=request.POST.get("system"),
            price=request.POST.get("price"),
            year=request.POST.get("year"),
            mileage=request.POST.get("mileage"),
            color=request.POST.get("color"),
            body_situation=request.POST.get("body_situation"),
            description=request.POST.get("description"),
        )
        car.save()
        images = request.FILES.getlist("images")
        for image in images:
            CarImg.objects.create(
                car=car,
                image=image,)
        return redirect("car_list")
    return render(request, "cars/add_car.html", context)



def car_info(request, id):
    car = get_object_or_404(
        Cars,
        id=id,)
    context = {
        "car": car,}
    return render(
        request,
        "cars/car_info.html",
        context,)
