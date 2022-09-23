# Generated by Django 3.2.5 on 2022-09-06 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20220827_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('material_color', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=7)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('threeD_model', models.FileField(blank=True, null=True, upload_to='gltf/')),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='pages.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='pages.product')),
            ],
        ),
    ]