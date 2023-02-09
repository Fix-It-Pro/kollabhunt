from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from ..managers.user_manager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=30, unique=True, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()
    def __str__(self):
        return self.email

    class Meta:
        managed = True
        db_table = 'kollabhunt_users'
