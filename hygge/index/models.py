from django.db import models

# Create your models here.

class ClothingItem(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='static/images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
