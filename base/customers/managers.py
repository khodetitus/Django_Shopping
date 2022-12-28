from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password):
        if not username:
            raise ValueError('user must have a username')
        if not email:
            raise ValueError('user must have an email')
        if not phone_number:
            raise ValueError('user must have a phone number')
        user = self.model(username=username, email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.create_user(username=username, email=email, phone_number=phone_number, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
