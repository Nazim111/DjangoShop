# Generated by Django 4.0.6 on 2022-07-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('bonus', models.IntegerField()),
                ('price', models.FloatField()),
                ('availability', models.BooleanField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('file', models.FileField(upload_to='product')),
            ],
        ),
    ]
