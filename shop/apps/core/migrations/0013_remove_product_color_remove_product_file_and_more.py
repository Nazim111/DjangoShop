# Generated by Django 4.0.6 on 2022-07-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='update_dt',
        ),
    ]
