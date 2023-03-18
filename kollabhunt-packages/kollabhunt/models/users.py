from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from ..managers.user_manager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=30, null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()
    def __str__(self):
        return self.email

    class Meta:
        managed = True
        db_table = 'kollabhunt_users'
