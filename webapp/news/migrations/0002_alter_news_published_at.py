# Generated by Django 5.1.7 on 2025-05-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="published_at",
            field=models.DateTimeField(verbose_name="Post published at"),
        ),
    ]
