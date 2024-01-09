# Generated by Django 4.2.8 on 2024-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pivots_manager", "0021_pivotreport_sent_to_bi"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="pivotreport",
            index=models.Index(
                fields=["sent_to_bi", "-start_time"], name="pivotreportsBISearch"
            ),
        ),
    ]