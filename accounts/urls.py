from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("user_page/<int:id>/", views.user_page, name="user_page"),
    path("edit_profile/<int:id>/", views.edit_profile, name="edit_profile"),
]
