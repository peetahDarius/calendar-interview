# Generated by Django 5.1 on 2024-08-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('guest', '0003_remove_guest_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(related_name='events', to='guest.guest'),
        ),
    ]
