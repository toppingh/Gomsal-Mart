# Generated by Django 3.2 on 2023-08-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='product_id',
        ),
    ]
