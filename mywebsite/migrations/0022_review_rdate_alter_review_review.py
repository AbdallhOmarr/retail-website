# Generated by Django 4.1.5 on 2023-04-26 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0021_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='RDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=500),
        ),
    ]
