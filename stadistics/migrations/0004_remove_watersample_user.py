# Generated by Django 4.2.3 on 2023-07-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stadistics', '0003_watersample_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watersample',
            name='user',
        ),
    ]
