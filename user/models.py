from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=13, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.username

class CustomUserRole(models.Model):
    role = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(CustomUser, related_name='roles', blank=True)


    def __str__(self):
        return self.role


class CustomUserPermission(models.Model):
    modules = models.ManyToManyField('CustomUserModule', related_name='permissions')
    roles = models.ManyToManyField('CustomUserRole', related_name='permissions')

    def __str__(self):
        role_names = ', '.join(role.role for role in self.roles.all())
        return f"Permission for roles: {role_names}"
    


class CustomUserModule(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null= True) 


    def __str__(self):
        return self.name
