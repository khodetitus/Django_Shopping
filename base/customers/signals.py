from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, Address


@receiver(post_save, sender=User)
def create_profile_address(sender, **kwargs):
    if kwargs.get('created', False):
        profile = Profile.objects.create(user=kwargs.get('instance'))
        Address.objects.create(profile=profile)
