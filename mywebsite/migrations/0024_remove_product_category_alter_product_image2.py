# Generated by Django 4.1.5 on 2023-05-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0023_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='product_images/', verbose_name='Image2'),
        ),
    ]