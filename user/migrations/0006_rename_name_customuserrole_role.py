# Generated by Django 4.2.7 on 2023-11-17 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_rename_role_customuserpermission_roles_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuserrole",
            old_name="name",
            new_name="role",
        ),
    ]
