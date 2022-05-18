
from django.db import models
# AbstractBaseUser > me permite modificar todo el modelo auth_user desde cero
# AbstractUser > me permite agregar nuevas columnas de las que ya estaban creadas inicialmente
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .authManager import UserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=45, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'correo'

    
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = 'usuarios'