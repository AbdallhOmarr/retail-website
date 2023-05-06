# Generated by Django 4.1.5 on 2023-04-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0020_alter_product_discountprice_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Mohamed Alashkar', max_length=20)),
                ('rate', models.DecimalField(decimal_places=1, default=0, max_digits=8)),
                ('review', models.CharField(max_length=100)),
            ],
        ),
    ]