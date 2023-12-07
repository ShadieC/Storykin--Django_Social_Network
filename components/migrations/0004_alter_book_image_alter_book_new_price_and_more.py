# Generated by Django 4.2.2 on 2023-07-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("components", "0003_article_image_book_image_book_new_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(upload_to="BookImages/"),
        ),
        migrations.AlterField(
            model_name="book",
            name="new_price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="book",
            name="old_price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]