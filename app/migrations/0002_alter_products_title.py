# Generated by Django 4.1.3 on 2023-01-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
