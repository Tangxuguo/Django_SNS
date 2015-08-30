from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Follow(models.Model):
    id = models.AutoField( primary_key = True )
    follower = models.ForeignKey(User,related_name='follower')
    followee = models.ForeignKey(User,related_name='followee')
    ts = models.DateTimeField( default = datetime.datetime.now() )