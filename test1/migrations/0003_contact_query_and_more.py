# Generated by Django 5.1.1 on 2024-09-15 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
                ('date_time', models.DateTimeField(default=datetime.datetime.today, verbose_name='Date')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_category',
            new_name='Product_Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_description',
            new_name='Product_Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_id',
            new_name='Product_ID',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_image',
            new_name='Product_Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='Product_Name',
        ),
    ]
