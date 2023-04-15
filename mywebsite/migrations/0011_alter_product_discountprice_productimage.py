# Generated by Django 4.1.5 on 2023-04-15 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0010_product_prdisbestseller_product_prdisnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount Price'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='prodcut/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywebsite.product', verbose_name='Product')),
            ],
        ),
    ]
