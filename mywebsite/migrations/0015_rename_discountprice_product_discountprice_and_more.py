# Generated by Django 4.1.5 on 2023-04-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0014_alter_product_discountprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discountPrice',
            new_name='discountprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='mainimage',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Image2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Image3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Image4'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]