# Generated by Django 3.2.3 on 2021-07-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_bid_bid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
