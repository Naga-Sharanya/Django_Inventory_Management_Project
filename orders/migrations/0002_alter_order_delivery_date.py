# Generated by Django 4.2.7 on 2023-11-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_date",
            field=models.DateField(),
        ),
    ]
