from django.db import models

# Create your models here.
class Scooter(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100,primary_key = True)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100,null = True)
    address = models.CharField(max_length = 500,null = True)
    age = models.IntegerField( default=18,
        validators=[
            MinValueValidator(18)
        ])
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

