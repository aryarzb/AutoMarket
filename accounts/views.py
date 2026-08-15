from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from cars.models import Cars
from django.contrib.auth.decorators import login_required


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
    
    
def logout_view(request):
    logout(request)
    return redirect("car_list")



@login_required
def profile(request):
    cars = request.user.cars.all()
    context = {
        "cars" : cars
    }
    return render(request, "accounts/profile.html", context)


def user_page(request, id):
    user = get_object_or_404(
        User,
        id=id
    )
    cars = Cars.objects.filter(
        owner=user
    )
    return render(
        request,
        "accounts/user_page.html",
        {
            "user": user,
            "cars": cars,
        },
    )
    
    
    
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