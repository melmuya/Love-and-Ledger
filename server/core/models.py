from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.email})"

    def get_full_name(self):
        """Get the user's full name"""
        return self.name

    def get_short_name(self):
        """Get the user's short name (first name)"""
        return self.name.split()[0] if self.name else self.name

