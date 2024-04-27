from django.db import models
from django.core.validators import  MinValueValidator

userType = (
    ("admin","Admin"),
    ("vendor","Vendor"),
    ("user","User")
)
# Create your models here.
class User(models.Model):
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

    def __str__(self):
        return self.name

