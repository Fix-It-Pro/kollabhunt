# Generated by Django 4.1.6 on 2023-02-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_stuff', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'kollabhunt_users',
                'managed': True,
            },
        ),
    ]