# Generated by Django 3.2.9 on 2021-12-13 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_user_userorder_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='customer',
            new_name='user',
        ),
    ]
