# Generated by Django 4.1.3 on 2022-11-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipment",
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
                ("brand", models.CharField(max_length=20)),
                ("model", models.CharField(max_length=20)),
                ("serial_number", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=150)),
                ("client", models.CharField(max_length=30)),
                ("center", models.CharField(max_length=50)),
                ("ubication", models.CharField(max_length=50)),
                ("reported", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
