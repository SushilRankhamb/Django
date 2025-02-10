from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.color}) - ${self.price}"
