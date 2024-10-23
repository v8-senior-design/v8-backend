import secrets
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def generate_unique_token(len):
    """
    * Generates random token (LEN=6)
    """
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(len))


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Regular User"""
        if not email:
            raise ValueError('Users must have a valid email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Admin User"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    * Custom User Model
    * Uses email as default field instead of username
    """
    email = models.CharField(max_length=70, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    dob = models.CharField(max_length=10, null=True)  # ! Later convert it to DateField
    profile_img = models.ImageField(null=True, upload_to='profile_imgs/')
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    @property
    def full_name(self):
        """
        * Display full name of the user
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.email} - {self.full_name}"
