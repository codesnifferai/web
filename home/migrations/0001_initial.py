# Generated by Django 4.2.4 on 2023-08-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CodeSnippet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.TextField()),
                ("score", models.FloatField()),
                ("created_at", models.DateTimeField(verbose_name="date created")),
            ],
        ),
    ]