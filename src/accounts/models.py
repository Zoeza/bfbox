from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# ------------ User Manager Class ---------------#

class UserManager(BaseUserManager):
    def _create_user(self, first_name, last_name, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
        return self._create_user(first_name, last_name, email, password, False, False, **extra_fields)

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        user = self._create_user(first_name, last_name, email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


# -------------- User Class ------------------#

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email


# ------------- User type Class -----------------#

class user_type(models.Model):
    is_manager = models.BooleanField(default=False)
    is_bailiff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_manager:
            return User.get_email(self.user) + " - is_manager"
        elif self.is_bailiff:
            return User.get_email(self.user) + " - is_bailiff"
        else:
            return User.get_email(self.user) + " - is_employee"
