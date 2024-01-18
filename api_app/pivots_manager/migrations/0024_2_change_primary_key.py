# Generated by Django 4.2.8 on 2024-01-09 14:31
import django
from django.contrib.postgres.expressions import ArraySubquery
from django.db import migrations, models


def migrate(apps, schema_editor):
    PivotConfig = apps.get_model("pivots_manager", "PivotConfig")
    PivotConfig.objects.update(
        disabled2=ArraySubquery(
            PivotConfig.objects.filter(pk=models.OuterRef("pk")).values(
                "disabled_in_organizations__pk"
            )
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ("playbooks_manager", "0024_1_change_primary_key"),
        ("pivots_manager", "0023_4_change_primary_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="pivotconfig",
            name="disabled2",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.RunPython(
            migrate,
        ),
        migrations.AlterField(
            model_name="pivotconfig",
            name="playbook_to_execute",
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name="pivotconfig", name="disabled_in_organizations"
        ),
    ]