from django.db import models
from django.conf import settings

class Color(models.TextChoices):
    WHITE = "white", "White"
    BLACK = "black", "Black"
    SILVER = "silver", "Silver"
    GRAY = "gray", "Gray"
    TITANIUM = "titanium", "Titanium"
    BLUE = "blue", "Blue"
    DARK_BLUE = "dark blue", "Dark Blue"
    RED = "red", "Red"
    DARK_RED = "dark red", "Dark Red"
    
    
class Body(models.TextChoices):
    CLEAN = "clean", "Clean"
    PARTIAL_PAINT = "partial painted", "Partial Painted"
    PAINTED = "painted", "Painted"
    PAINTLESS_DENT_REPAIR = "paintless dent repair", "Paintless Dent Repair"
    BODY_REPAIR = "body repair", "Body Repair"
    REPLACED = "replaced", "Replaced"
    
    

class Cars(models.Model):
    brand = models.CharField(max_length=60);
    system = models.CharField(max_length=100);
    year = models.IntegerField();
    price = models.IntegerField(default=0);
    mileage = models.IntegerField();
    color = models.CharField(max_length=50, choices=Color.choices);
    body_situation = models.CharField(max_length=50, choices=Body.choices);
    description = models.TextField(default="null");
    owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="cars"
)
    
    
class CarImg(models.Model):
        car = models.ForeignKey(
        "Cars",
        on_delete=models.CASCADE,
            related_name="images",)
        image = models.ImageField(
            upload_to="cars/",)
        uploaded_at = models.DateTimeField(
            auto_now_add=True,)

        def __str__(self):
            return f"{self.car.brand} Image"
    
