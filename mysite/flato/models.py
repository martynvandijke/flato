from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from autoslug import AutoSlugField


##store data wich belongs to the user itself
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wheater_city = models.CharField(max_length=200,default="Eindhoven")
    wheater_degree = models.CharField(max_length=10,default="celsius")
    wheater_citykey = models.TextField(null=True, blank=True)
    wheater_country = models.TextField(null=True, blank=True)
    wheater_province = models.TextField(null=True, blank=True)
    wheater_dailyforecasts = models.TextField(null=True, blank=True)
    wheater_today = models.TextField(null=True, blank=True)

## create extended user profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

## save extended user profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Frontpage(models.Model):
    image = models.TextField(null=True, blank=True)

## news model
class News(models.Model):
    source = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)