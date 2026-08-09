from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from cars.models import Cars


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect("car_list")
        
        else:
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")

User = get_user_model()
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        mobile_number = request.POST.get("mobile_number")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        state = request.POST.get("state")
        city = request.POST.get("city")
        if password != confirm_password:
            return render(request, "accounts/register.html")
        if User.objects.filter(mobile_number=mobile_number).exists():
            return render(request, "accounts/register.html")
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        user.first_name = first_name
        user.last_name = last_name
        user.state = state
        user.city = city
        user.mobile_number = mobile_number
        user.save()
        return redirect("login")
    return render(request, "accounts/register.html")




def car_info(request, id):

    car = get_object_or_404(
        Cars ,
        id=id
    )
    return render(
        request,
        "cars/car_info.html",
        {
            "car": car,
        },
    )