# Generated by Django 4.1 on 2023-12-11 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_vendorrequest_tin_check_vendorrequest_w9_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vendorReview',
            new_name='reviewVendor',
        ),
    ]
