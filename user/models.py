from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    school_id =models.CharField(unique=True,
                                 error_messages={
                                     'unique':_('A student with that id number already exists')
                                 },
                                 max_length=10,
                                 primary_key=True   )

    email = models.EmailField(_('email address'),unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'school_id'
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.school_id
