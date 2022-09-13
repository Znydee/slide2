# Generated by Django 4.0.3 on 2022-06-18 09:31

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='nothing-to-show', editable=True, populate_from='bio', unique=True),
        ),
    ]