# Generated by Django 4.0.6 on 2022-07-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_checkin_alter_booking_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateField(),
        ),
    ]
