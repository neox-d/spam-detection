from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
import uuid


class MyUserManager(BaseUserManager):

    def create_user(self, name, phone, password=None, email=None):
        """
        Creates and saves a User with the given name, phone number and password
        """
        if not (name and phone):
            raise ValueError("Users must enter a name and phone number")

        user = self.model(
            name = name,
            phone = phone
        ) 

        if email:
            user.email = self.normalize_email(email)

        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, name, phone, password=None, email=None):
        """
        Creates and saves a superuser with the given name, phone number and password
        """

        user = self.create_user(name, password=password, phone=phone)

        if email:
            user.email = email

        user.is_admin = True
        user.save()
        return user


class MyUser(AbstractUser):

    use_in_migrations = True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    name = models.CharField(max_length=200)
    phone = models.CharField(verbose_name="phone number", max_length=15, unique=True)
    email = models.EmailField(verbose_name="email address", max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return f'{self.name} - {self.phone}'