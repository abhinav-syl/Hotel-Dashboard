# Generated by Django 4.0.6 on 2022-07-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.IntegerField(default=2500),
        ),
    ]
