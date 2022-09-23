# Generated by Django 3.2.5 on 2022-08-27 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]