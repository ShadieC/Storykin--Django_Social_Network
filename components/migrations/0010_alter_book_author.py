# Generated by Django 4.2.2 on 2023-08-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("components", "0009_rename_author_articlereadingactivity_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=255),
        ),
    ]