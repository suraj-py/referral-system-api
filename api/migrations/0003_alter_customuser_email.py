# Generated by Django 4.2.11 on 2024-04-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_remove_customuser_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
