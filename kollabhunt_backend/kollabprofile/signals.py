from django.db.models.signals import post_save
from django.dispatch import receiver
from kollabhunt.models.users import User
from kollabhunt.models.profile import KollabProfile


@receiver(post_save, sender=User)
def create_kollab_profile(sender, instance, created, **kwargs):
    if created:
        KollabProfile.objects.create(user=instance)
        print("profile is created!")