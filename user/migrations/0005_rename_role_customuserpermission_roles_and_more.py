# Generated by Django 4.2.7 on 2023-11-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_customuserpermission_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuserpermission",
            old_name="role",
            new_name="roles",
        ),
        migrations.AddField(
            model_name="customuserrole",
            name="modules",
            field=models.ManyToManyField(
                related_name="roles", to="user.customusermodule"
            ),
        ),
    ]
