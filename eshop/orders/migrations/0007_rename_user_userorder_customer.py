# Generated by Django 3.2.9 on 2021-12-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_customer_userorder_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='user',
            new_name='customer',
        ),
    ]
