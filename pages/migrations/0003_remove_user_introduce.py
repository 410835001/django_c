# Generated by Django 3.2.5 on 2022-07-27 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='introduce',
        ),
    ]