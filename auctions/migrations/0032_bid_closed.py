# Generated by Django 3.2.3 on 2021-08-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_auto_20210802_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]