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
            is_admin=kwargs.get('is_admin', ''),
            is_superuser=kwargs.get('is_superuser', ''),
            is_stuff=kwargs.get('is_stuff', ''),
        )
        user.set_password()
        user.save(using=self._db)
        return user
