from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError("Email not provided")
        if not username:
            raise ValueError("Username not provided")
        if not password:
            raise ValueError("Password not provided")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=kwargs.get('firstname', ''),
            lastname=kwargs.get('lastname', ''),
            is_admin=False,
            is_superuser=False,
            is_staff=kwargs.get('is_staff', False),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password, **kwargs):
        if not email:
            raise ValueError("Email not provided")
        if not username:
            raise ValueError("Username not provided")
        if not password:
            raise ValueError("Password not provided")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=kwargs.get('firstname', ''),
            lastname=kwargs.get('lastname', ''),
            is_admin=True,
            is_superuser=True,
            is_staff=kwargs.get('is_staff', True),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
