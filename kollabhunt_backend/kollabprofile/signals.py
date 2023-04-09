import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from kollabhunt.models.users import User
from kollabhunt.models.profile import KollabProfile
from allauth.socialaccount.models import SocialAccount


@receiver(post_save, sender=User)
def create_kollab_profile(sender, instance, created, **kwargs):
    if created:
        social_info = SocialAccount.objects.filter(instance.id)
        extra_info = json.loads(social_info.first().extra_data)
        user_info = {
            'user': instance
        }
        if social_info.provider == 'github_auth':
            user_info.update({
                'image': extra_info.avatar_url,
                'bio': extra_info.bio
            })
        elif social_info.provider == 'google_auth':
            user_info.update({
                'image': extra_info.picture
            })
        KollabProfile.objects.create(**user_info)
        print("profile is created!")