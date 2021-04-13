# Generated by Django 3.2 on 2021-04-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_crud_device_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='device_model',
            field=models.TextField(default='ABXCDN', max_length=100),
        ),
        migrations.AddField(
            model_name='crud',
            name='device_price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='crud',
            name='device_weight',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='crud',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]