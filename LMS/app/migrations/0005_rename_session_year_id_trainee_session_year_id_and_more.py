# Generated by Django 4.2 on 2023-04-18 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_customuser_user_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trainee",
            old_name="session_Year_id",
            new_name="session_year_id",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[(1, "Manager"), (2, "Mentor"), (3, "Trainee")],
                default="Manager",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="Mentor",
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
                ("adddress", models.TextField()),
                ("gender", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]