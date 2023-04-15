# Generated by Django 4.1.5 on 2023-04-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0011_alter_product_discountprice_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='PRDIProduct',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='PRDIImage',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='prodcut/', verbose_name='Image2'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='prodcut/', verbose_name='Image3'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='prodcut/', verbose_name='Image4'),
        ),
    ]
