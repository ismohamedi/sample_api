# Generated by Django 4.0.1 on 2022-01-20 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="create_on",
            new_name="created_on",
        ),
    ]
