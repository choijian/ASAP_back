# Generated by Django 4.1.13 on 2024-02-13 03:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="aaa", max_length=20),
            preserve_default=False,
        ),
    ]