# Generated by Django 2.0.7 on 2018-08-31 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_userprofileinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_pic',
            new_name='profile_pic',
        ),
    ]