from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Piado(models.Model):
  text = models.CharField(max_length=140)
  user = models.ForeignKey(User)

class Follow(models.Model):
  follower_user = models.ForeignKey(User,related_name="follower")
  followed_user = models.ForeignKey(User,related_name="followed")
