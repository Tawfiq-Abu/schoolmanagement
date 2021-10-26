from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
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
