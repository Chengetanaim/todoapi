# Generated by Django 4.1 on 2022-09-02 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]