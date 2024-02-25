from django.db import models
from User.models import User

# Create your models here.
class Scooter(models.Model):
    id = models.IntegerField(primary_key = True)
    color = models.CharField(max_length = 50)
    model = models.CharField(max_length = 100)
    rate_per_hour = models.FloatField(default = 0.0)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.model
    
    @property
    def time_diff(self,start_time,end_time):
        return self.end_time - self.start_time

