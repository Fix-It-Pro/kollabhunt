# Generated by Django 4.1.6 on 2023-03-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kollabhunt', '0002_rename_is_stuff_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True, verbose_name='email'),
        ),
    ]