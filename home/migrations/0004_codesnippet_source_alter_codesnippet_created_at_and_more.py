# Generated by Django 4.2.4 on 2023-08-30 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_codesnippet_udpated_at_scores_udpated_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="codesnippet",
            name="source",
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="codesnippet",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="codesnippet",
            name="udpated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="scores",
            name="code",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scores",
                to="home.codesnippet",
                verbose_name="CodeSnippet",
            ),
        ),
        migrations.AlterField(
            model_name="scores",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="scores",
            name="udpated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]