# Generated by Django 4.2.2 on 2023-08-02 19:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_profile_bio_profile_first_name_profile_last_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
    ]
