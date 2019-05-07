from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# from campaigns.models import CampaignPartyRelation
# from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    # No other data for now


# @receiver(post_save, sender=User)
# def create_user_profile (sender, instance, **kwargs):
#
#     user_profile = UserProfile(user=instance)
#     user_profile.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
