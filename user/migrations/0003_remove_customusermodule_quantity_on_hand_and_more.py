# Generated by Django 4.2.7 on 2023-11-16 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_customusermodule_quantity_on_hand_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customusermodule",
            name="quantity_on_hand",
        ),
        migrations.RemoveField(
            model_name="customusermodule",
            name="vendor",
        ),
    ]
