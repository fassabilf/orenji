# Generated by Django 5.1.1 on 2024-09-05 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_orenjientry_delete_moodentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orenjientry',
            old_name='decription',
            new_name='descriptions',
        ),
    ]
