# Generated by Django 4.0.4 on 2023-04-10 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0005_remove_product_category_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_zip_code',
        ),
    ]
