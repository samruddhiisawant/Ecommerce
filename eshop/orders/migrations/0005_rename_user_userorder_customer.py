# Generated by Django 3.2.9 on 2021-12-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderdetails_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='user',
            new_name='customer',
        ),
    ]