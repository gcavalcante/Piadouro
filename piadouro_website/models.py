from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Piado(models.Model):
  text = models.CharField(max_length=140)
  user = models.ForeignKey(User)
  date_time = models.DateTimeField(datetime.datetime.now())

class Follow(models.Model):
  follower_user = models.ForeignKey(User,related_name="follower")
  followed_user = models.ForeignKey(User,related_name="followed")
