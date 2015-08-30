# coding=utf-8
from django.db import models
import datetime

# Create your models here.
class Tag (models.Model):
	id = models.AutoField( primary_key = True )
	name = models.CharField( max_length = 100, blank=True )
	add_ts = models.DateTimeField( default = datetime.datetime.now() )
	cover = models.URLField(blank=True)