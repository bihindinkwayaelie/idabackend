# Generated by Django 4.1.1 on 2022-10-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='fullname',
            new_name='sender',
        ),
    ]
