# Generated by Django 3.0.6 on 2020-09-20 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
