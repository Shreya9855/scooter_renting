from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import  MinValueValidator

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        if not username:
            raise ValueError('The Username fiels must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


userType = (
    ("admin","Admin"),
    ("vendor","Vendor"),
    ("user","User")
)
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100,primary_key = True)
    email = models.CharField(max_length = 100,null=True)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100,null = True)
    address = models.CharField(max_length = 500,null = True)
    age = models.IntegerField( default=18,
        validators=[
            MinValueValidator(18)
        ])
    amount = models.FloatField(default=0)
    userType = models.CharField( 
        max_length = 20, 
        choices = userType, 
        default = "user"
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)  # Ensure this field is present
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid conflict with auth.User.groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Avoid conflict with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

