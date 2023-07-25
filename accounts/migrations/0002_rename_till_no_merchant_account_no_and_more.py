# Generated by Django 4.2 on 2023-04-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="merchant",
            old_name="till_no",
            new_name="account_no",
        ),
        migrations.RenameField(
            model_name="merchant",
            old_name="image",
            new_name="business_image",
        ),
        migrations.AddField(
            model_name="merchant",
            name="business_description",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="merchant",
            name="business_name",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
