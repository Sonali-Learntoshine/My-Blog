# Generated by Django 3.1.2 on 2021-01-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]