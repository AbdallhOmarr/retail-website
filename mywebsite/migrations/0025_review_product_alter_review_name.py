# Generated by Django 4.1.5 on 2023-05-07 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0024_remove_product_category_alter_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mywebsite.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
