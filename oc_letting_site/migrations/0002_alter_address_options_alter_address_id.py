# Generated by Django 4.2.7 on 2023-11-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("oc_letting_site", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Address", "verbose_name_plural": "Addresses"},
        ),
        migrations.AlterField(
            model_name="address",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
