from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.car_list, name="car_list"),
    path("add_car/", views.add_car, name="add_car"),
    path("cars/<int:id>", views.car_info, name="car_info"),
    path("delete-car/<int:id>/", views.delete_car, name="delete_car"),
    path("edit_profile/<int:id>/", views.edit_profile, name="edit_profile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )