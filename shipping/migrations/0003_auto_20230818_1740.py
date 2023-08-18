# Generated by Django 3.2 on 2023-08-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('shipping', '0002_auto_20230818_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='product',
        ),
        migrations.AddField(
            model_name='shipping',
            name='products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
    ]
