# Generated by Django 5.0.4 on 2024-04-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Machine",
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
                ("name", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="machine_photos")),
                ("manufacturer", models.CharField(max_length=100)),
                ("year_manufactured", models.IntegerField()),
                ("serial_number", models.CharField(max_length=50)),
                ("machine_type", models.CharField(max_length=100)),
            ],
        ),
    ]
