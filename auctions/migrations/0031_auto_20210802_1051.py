# Generated by Django 3.2.3 on 2021-08-02 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_listing_last_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='user_id',
            new_name='user',
        ),
    ]
