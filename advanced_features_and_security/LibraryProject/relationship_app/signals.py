# django-models/LibraryProject/relationship_app/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a UserProfile whenever a User is saved.
    """
    if created:
        # If a new User is created, create a corresponding UserProfile
        UserProfile.objects.create(user=instance)
    # If the user already exists, ensure their profile is saved (useful if profile fields change)
    # instance.userprofile.save() # Uncomment if you want to ensure existing profiles are saved on user save