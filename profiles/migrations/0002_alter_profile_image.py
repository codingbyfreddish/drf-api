# Generated by Django 3.2.20 on 2023-07-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_gk7dwg', upload_to='images/'),
        ),
    ]
