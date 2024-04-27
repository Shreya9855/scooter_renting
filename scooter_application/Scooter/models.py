from django.db import models
from User.models import User
from django.utils import timezone


# Create your models here.
class Scooter(models.Model):
    id = models.IntegerField(primary_key = True)
    color = models.CharField(max_length = 50)
    model = models.CharField(max_length = 100)
    rate_per_hour = models.FloatField(default = 0.0)
    vendor_id = models.ForeignKey(User,on_delete = models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default = False)
    user_id = models.CharField(max_length = 100)
    image = models.ImageField(
            upload_to='static/images/uploads', 
            # height_field='800', 
            # width_field='600', 
            # max_length=100,
            default='default_scooter_image.jpg')

    def __str__(self):
        return self.model
    
    @property
    def time_diff(self,start_time,end_time):
        return self.end_time - self.start_time