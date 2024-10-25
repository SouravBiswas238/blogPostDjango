from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class ParentModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=50, null=True, blank=True)
    is_trial = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    attributes = models.JSONField(default=dict, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        unique_together = ['email', "username"]
