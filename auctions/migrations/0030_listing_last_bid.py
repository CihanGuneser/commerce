# Generated by Django 3.2.3 on 2021-07-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_auto_20210730_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='last_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]