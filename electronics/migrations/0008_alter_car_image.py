# Generated by Django 5.1.6 on 2025-02-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0007_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]
