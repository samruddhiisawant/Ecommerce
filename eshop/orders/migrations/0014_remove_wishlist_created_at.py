# Generated by Django 3.2.9 on 2021-12-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_wishlist_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='created_at',
        ),
    ]
