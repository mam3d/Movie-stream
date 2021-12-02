from django.db import models
from django.contrib.auth.models import (
                    AbstractBaseUser,
                    BaseUserManager,
                    PermissionsMixin
                    )
from django.core.exceptions import ValidationError
from .validators import phone_validator



class CustomUserManager(BaseUserManager):
    def create_user(self,phone,password):
        user = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,phone,password):
        user = self.model(phone=phone)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(unique=True,max_length=11,validators=[phone_validator])
    name = models.CharField(max_length=100,blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    def __str__(self):
        if self.name:
            return self.name
        return self.phone


class PhoneVerify(models.Model):
    phone = models.CharField(max_length=11)
    code = models.IntegerField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = "phone verifies"
