# Generated by Django 3.2 on 2021-04-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_crud_device_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='device_image',
            field=models.ImageField(upload_to='crud/'),
        ),
        migrations.AlterField(
            model_name='crud',
            name='device_model',
            field=models.CharField(max_length=100),
        ),
    ]
