# Generated by Django 2.2.5 on 2019-09-17 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guild',
            old_name='create',
            new_name='created',
        ),
    ]
