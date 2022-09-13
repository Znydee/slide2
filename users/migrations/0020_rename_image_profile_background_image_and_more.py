# Generated by Django 4.0.6 on 2022-08-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='background_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures'),
        ),
    ]
