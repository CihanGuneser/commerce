# Generated by Django 3.2.3 on 2021-07-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_rename_most_recent_bid_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/%d'),
        ),
    ]
