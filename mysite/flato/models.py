from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


## news model
class News(models.Model):
    news_source = models.TextField(null=True, blank=True)
    news_title = models.TextField(null=True, blank=True)
    news_description = models.TextField(null=True, blank=True)
    news_date = models.TextField(null=True, blank=True)
    news_author = models.TextField(null=True, blank=True)
    news_image = models.TextField(null=True, blank=True)
    news_link = models.TextField(null=True, blank=True)