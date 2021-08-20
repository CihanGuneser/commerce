# Generated by Django 3.2.3 on 2021-08-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auto_20210811_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32)),
                ('listing', models.ManyToManyField(blank=True, default=None, related_name='category', to='auctions.Listing')),
            ],
        ),
    ]