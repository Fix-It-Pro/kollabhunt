# Generated by Django 4.1.6 on 2023-03-19 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kollabhunt', '0005_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=600)),
                ('description', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_project', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owned_project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kollabhunt_projects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=600, unique=True)),
                ('Tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kollabhunt.tag')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_tag', to='kollabhunt.project')),
            ],
            options={
                'db_table': 'kollabhunt_project_tags',
                'managed': True,
            },
        ),
    ]
