# Generated by Django 3.2.3 on 2021-07-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_image_link',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.ImageField(blank=True, upload_to='static/img/%Y/%m/%d'),
        ),
    ]
