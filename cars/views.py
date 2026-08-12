from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars, Color, Body, CarImg
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

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
            price=request.POST.get("price").replace(".", ""),
            year=request.POST.get("year"),
            mileage=request.POST.get("mileage").replace(".", ""),
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




@login_required
def delete_car(request, id):
    car = get_object_or_404(
        Cars,
        id=id,
        owner=request.user
    )
    if request.method == "POST":
        car.delete()
    return redirect("profile")



User = get_user_model()
@login_required
def edit_profile(request, id):

    user = get_object_or_404(
        User,
        id=id
    )
    if request.user != user:
        return redirect("profile")
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        mobile_number = request.POST.get("mobile_number")
        state = request.POST.get("state")
        city = request.POST.get("city")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if User.objects.filter(
            username=username
        ).exclude(
            id=user.id
        ).exists():
            return render(
                request,
                "accounts/edit_profile.html",
                {
                    "user": user,
                    "error": "This username is already taken."
                }
            )
        if User.objects.filter(
            mobile_number=mobile_number
        ).exclude(
            id=user.id
        ).exists():
            return render(
                request,
                "accounts/edit_profile.html",
                {
                    "user": user,
                    "error": "This mobile number is already registered."
                }
            )
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.mobile_number = mobile_number
        user.state = state
        user.city = city
        if password:
            if password != confirm_password:
                return render(
                    request,
                    "accounts/edit_profile.html",
                    {
                        "user": user,
                        "error": "Passwords do not match."
                    }
                )
            user.set_password(password)
        user.save()
        if password:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(
                request,
                user
            )
        return redirect("profile")
    return render(
        request,
        "accounts/edit_profile.html",
        {
            "user": user
        }
    )