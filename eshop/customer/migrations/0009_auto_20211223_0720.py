# Generated by Django 3.2.9 on 2021-12-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_banner_cms_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='modify_by',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='note_admin',
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='contact_no',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
