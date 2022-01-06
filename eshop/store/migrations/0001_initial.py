# Generated by Django 3.2.9 on 2021-12-09 05:58

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Available'), (0, 'Not Available')])),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_modify_by_user', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('modify_date', models.DateField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=45)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('special_price', models.FloatField()),
                ('special_price_from', models.DateField()),
                ('quantity', models.IntegerField()),
                ('meta_description', models.TextField()),
                ('meta_keyword', models.TextField()),
                ('status', models.BooleanField()),
                ('is_feature', models.BooleanField()),
                ('created_date', models.DateField(auto_now=True)),
                ('cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item_id', to='store.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_modify_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product_Attribute',
            fields=[
                ('created_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_modify_by_user', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('status', models.IntegerField(choices=[(1, 'Available'), (0, 'Not Available')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Attribute_values',
            fields=[
                ('created_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_Attribute_value', models.CharField(max_length=45)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_values_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_values_modify_by_user', to=settings.AUTH_USER_MODEL)),
                ('product_attribute_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.product_attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product_attribute_association',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product_attribute')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('product_attribute_value_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product_attribute_values')),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now_add=True)),
                ('code', models.CharField(max_length=45, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField()),
                ('no_of_uses', models.IntegerField(verbose_name='No of Uses:')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons_modify_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]