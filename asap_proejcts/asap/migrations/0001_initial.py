# Generated by Django 4.1.13 on 2024-02-19 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CommonInfo",
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
                ("image", models.ImageField(upload_to="input_image")),
                ("store_name", models.CharField(max_length=50)),
                ("purpose", models.CharField(max_length=50)),
                ("result_type", models.CharField(max_length=10)),
                ("theme", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ItemInfo",
            fields=[
                (
                    "commoninfo_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="asap.commoninfo",
                    ),
                ),
                ("product_name", models.CharField(max_length=50)),
                ("price", models.CharField(blank=True, max_length=20)),
                ("description", models.TextField()),
                ("business_hours", models.CharField(blank=True, max_length=30)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("contact", models.CharField(blank=True, max_length=20)),
                ("summarized_copy", models.CharField(blank=True, max_length=100)),
            ],
            bases=("asap.commoninfo", models.Model),
        ),
    ]
