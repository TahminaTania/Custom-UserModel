from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# ---> for customising user model 

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.
class managers(BaseUserManager):
    def create_user(self, email,username, password):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email))

        user.is_admin = True
        user.is_active =True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class profiles(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="last login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = managers()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIRLDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
# 
    # profile_image = models.ImageField(max_length=200, null=True, blank=True)


class subscriber(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
