from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.name = f'{self.first_name} {self.last_name}'.strip()
        super().save(*args, **kwargs)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    start_date = models.DateField()
    contract_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Client {self.client_id} - {self.user.username}'
