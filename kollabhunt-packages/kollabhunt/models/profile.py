from django.db import models
from .base_model import BaseModel


class KollabProfile(BaseModel):
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='kollab_user')
    image = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'kollabhunt_profile'


class KollabProfileTag(BaseModel):
    name = models.CharField(max_length=600, blank=False, null=False, unique=True)
    project = models.ForeignKey('KollabProfile', on_delete=models.CASCADE, blank=False, null=False, related_name='profile_tag')
    Tag = models.ForeignKey('Tag', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'kollabhunt_profile_tags'
