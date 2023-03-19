from .base_model import BaseModel
from django.db import models

class Project(BaseModel):
    name = models.CharField(max_length=600, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('User', on_delete=models.PROTECT, blank=True, null=True, related_name='owned_project')
    creator = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='created_project')

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'kollabhunt_projects'