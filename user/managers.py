from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 

class CustomUserManager(BaseUserManager):
    '''
    custom user model manager where school_id is the unique identifier
    for authentication instead of user name
    '''

    def create_user(self,school_id,email,password,**extra_fields):
        '''
        create and save a user with the given school_id and password
        '''
        if not school_id:
            raise ValueError(_('the school_id must be set'))
        email = self.normalize_email(email)
        user = self.model(school_id=school_id,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, school_id, email,password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(school_id,email, password, **extra_fields)