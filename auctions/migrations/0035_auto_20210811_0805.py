# Generated by Django 3.2.3 on 2021-08-11 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_rename_listing_id_comment_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_time',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_title',
            new_name='title',
        ),
    ]