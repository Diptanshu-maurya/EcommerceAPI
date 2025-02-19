from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class CustomManager(BaseUserManager):
  def create_user(self,email,password=None,**extra_fields):
    if not email:
      raise ValueError("email is must")
    email=self.normalize_email(email)
    user=self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save()
    return user
  def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)




class CustomUser(AbstractUser):
  username=None
  email=models.EmailField("email_address",unique=True)
  address = models.CharField(max_length=255, blank=True, null=True) 
  USERNAME_FIELD="email"
  REQUIRED_FIELDS = ['first_name', 'last_name']
  objects=CustomManager()

  def __str__(self):
    return self.email


