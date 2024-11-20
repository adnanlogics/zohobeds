from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Owner', 'Owner'),
        ('Employee', 'Employee'),
    ])
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Change the related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Change the related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )