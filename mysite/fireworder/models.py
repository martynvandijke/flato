from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room_status = models.CharField(max_length=10,default="on")
    wheater_city = models.CharField(max_length=200,default="Eindhoven")
    wheater_degree = models.CharField(max_length=10,default="on")
    wheater_satus = models.CharField(max_length=10,default="on")
    daily_status = models.CharField(max_length=10,default="on")
    verge_status = models.CharField(max_length=10,default="on")
    stock_status = models.CharField(max_length=10,default="on")
    movie_status = models.CharField(max_length=10,default="on")
    f1_status = models.CharField(max_length=10,default="on")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Data(models.Model):
    f1_round = models.TextField(null=True, blank=True)
    f1_season = models.TextField(null=True, blank=True)
    f1_wiki = models.TextField(null=True, blank=True)
    f1_name = models.TextField(null=True, blank=True)
    f1_date = models.TextField(null=True, blank=True)
    f1_time = models.TextField(null=True, blank=True)
    movie_poster = models.TextField(null=True, blank=True)
    movie_vote = models.TextField(null=True, blank=True)
    movie_title = models.TextField(null=True, blank=True)
    movie_overview = models.TextField(null=True, blank=True)
    verge_author = models.TextField(null=True, blank=True)
    verge_title = models.TextField(null=True, blank=True)
    verge_description = models.TextField(null=True, blank=True)
    verge_url = models.TextField(null=True, blank=True)
    verge_image = models.TextField(null=True, blank=True)
    wheater_cirtykey = models.TextField(null=True, blank=True)
    wheater_country = models.TextField(null=True, blank=True)
    wheater_province = models.TextField(null=True, blank=True)
    wheater_dailyforecasts = models.TextField(null=True, blank=True)
    wheater_today = models.TextField(null=True, blank=True)
    wheater_day1_min = models.TextField(null=True, blank=True)
    wheater_day1_max = models.TextField(null=True, blank=True)
    wheater_day1_icon = models.TextField(null=True, blank=True)
    wheater_day2 = models.TextField(null=True, blank=True)
    wheater_day2_min = models.TextField(null=True, blank=True)
    wheater_day2_max = models.TextField(null=True, blank=True)
    wheater_day2_icon = models.TextField(null=True, blank=True)
    wheater_day3_min = models.TextField(null=True, blank=True)
    wheater_day3_max = models.TextField(null=True, blank=True)
    wheater_day3_icon = models.TextField(null=True, blank=True)
    wheater_day4_min = models.TextField(null=True, blank=True)
    wheater_day4_max = models.TextField(null=True, blank=True)
    wheater_day4_icon = models.TextField(null=True, blank=True)
    wheater_day5_min = models.TextField(null=True, blank=True)
    wheater_day5_max = models.TextField(null=True, blank=True)
    wheater_day5_icon = models.TextField(null=True, blank=True)
    daily_imageurl = models.TextField(null=True, blank=True)
    daily_imagelink = models.TextField(null=True, blank=True)
    stock_companyname = models.TextField(null=True, blank=True)
    stock_exchange = models.TextField(null=True, blank=True)
    stock_price = models.TextField(null=True, blank=True)
    stock_changepercent = models.TextField(null=True, blank=True)
