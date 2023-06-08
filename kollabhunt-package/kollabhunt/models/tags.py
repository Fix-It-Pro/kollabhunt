from django.db import models
from  .base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'kollabhunt_tags'


class ProjectTag(BaseModel):
    name = models.CharField(max_length=600, blank=False, null=False, unique=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=False, null=False, related_name='project_tag')
    Tag = models.ForeignKey('Tag', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'kollabhunt_project_tags'
