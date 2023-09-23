from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class C_user(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
