from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from staff.common import StaffCommonFields
from staff.managers import CustomUserManager


class Staff(StaffCommonFields, AbstractBaseUser, PermissionsMixin):
    # Staff is responsible for setting up sellers account.
    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

