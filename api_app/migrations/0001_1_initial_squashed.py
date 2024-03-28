# Generated by Django 4.2.8 on 2024-02-08 07:51
import datetime

import django.contrib.postgres.fields
import django.core.validators
import django.db.migrations.operations.special
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import api_app.defaults
import api_app.validators


def migrate_bi(apps, schema_editor):
    from intel_owl.celery import get_queue_name

    CrontabSchedule = apps.get_model("django_celery_beat", "CrontabSchedule")
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")

    # notification

    c1 = CrontabSchedule.objects.get_or_create(minute=12)[0]
    PeriodicTask.objects.create(
        name="send_elastic_bi",
        task="intel_owl.tasks.send_bi_to_elastic",
        crontab=c1,
        enabled=settings.ELASTICSEARCH_BI_ENABLED,
        queue=get_queue_name("default"),
    )


def reverse_migrate_bi(apps, schema_editor):
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")
    PeriodicTask.objects.filter(name="send_elastic_bi").delete()


def create_default_clients(apps, schema_editor):
    # We can't import the Client model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Client = apps.get_model("durin", "Client")
    # for pyintelowl, custom token_ttl
    Client.objects.update_or_create(
        name="pyintelowl", token_ttl=datetime.timedelta(weeks=4 * 12 * 10)
    )
    # others, default token_ttl
    Client.objects.update_or_create(name="web-browser")
    _ = Client.objects.get_or_create(
        name=settings.REST_DURIN["API_ACCESS_CLIENT_NAME"],
        token_ttl=settings.REST_DURIN["API_ACCESS_CLIENT_TOKEN_TTL"],
    )


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("certego_saas_organization", "0001_initial"),
        ("django_celery_beat", "0018_improve_crontab_helptext"),
        ("durin", "0002_client_throttlerate"),
    ]
    initial = True
    operations = [
        migrations.CreateModel(
            name="Tag",
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
                (
                    "label",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(4)],
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", "Hex color"
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("is_sample", models.BooleanField(default=False)),
                ("md5", models.CharField(max_length=32)),
                ("observable_name", models.CharField(blank=True, max_length=512)),
                (
                    "observable_classification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ip", "Ip"),
                            ("url", "Url"),
                            ("domain", "Domain"),
                            ("hash", "Hash"),
                            ("generic", "Generic"),
                            ("", "Empty"),
                        ],
                        max_length=12,
                    ),
                ),
                ("file_name", models.CharField(blank=True, max_length=512)),
                ("file_mimetype", models.CharField(blank=True, max_length=80)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("running", "running"),
                            ("analyzers_running", "analyzers_running"),
                            ("analyzers_completed", "analyzers_completed"),
                            ("connectors_running", "connectors_running"),
                            ("connectors_completed", "connectors_completed"),
                            ("pivots_running", "pivots_running"),
                            ("pivots_completed", "pivots_completed"),
                            ("visualizers_running", "visualizers_running"),
                            ("visualizers_completed", "visualizers_completed"),
                            ("reported_without_fails", "reported_without_fails"),
                            ("reported_with_fails", "reported_with_fails"),
                            ("killed", "killed"),
                            ("failed", "failed"),
                        ],
                        default="pending",
                        max_length=32,
                    ),
                ),
                (
                    "received_request_time",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                ("finished_analysis_time", models.DateTimeField(blank=True, null=True)),
                (
                    "errors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=900),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True, upload_to=api_app.defaults.file_directory_path
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="jobs", to="api_app.tag"
                    ),
                ),
                (
                    "tlp",
                    models.CharField(
                        choices=[
                            ("CLEAR", "Clear"),
                            ("GREEN", "Green"),
                            ("AMBER", "Amber"),
                            ("RED", "Red"),
                        ],
                        default="CLEAR",
                        max_length=8,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("process_time", models.FloatField(blank=True, null=True)),
                (
                    "runtime_configuration",
                    models.JSONField(
                        default=api_app.defaults.default_runtime,
                        validators=[api_app.validators.validate_runtime_configuration],
                    ),
                ),
                (
                    "scan_check_time",
                    models.DurationField(
                        blank=True, default=datetime.timedelta(days=1), null=True
                    ),
                ),
                (
                    "scan_mode",
                    models.IntegerField(
                        choices=[
                            (1, "Force New Analysis"),
                            (2, "Check Previous Analysis"),
                        ],
                        default=2,
                    ),
                ),
                ("sent_to_bi", models.BooleanField(default=False, editable=False)),
                (
                    "warnings",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["md5", "status"], name="api_app_job_md5_4d2c5e_idx"
                    )
                ],
            },
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["sent_to_bi", "-received_request_time"], name="JobBISearch"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="api_app.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.RunPython(
            code=create_default_clients,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.RunPython(
            code=migrate_bi,
            reverse_code=reverse_migrate_bi,
        ),
        migrations.CreateModel(
            name="PythonModule",
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
                ("module", models.CharField(db_index=True, max_length=120)),
                (
                    "base_path",
                    models.CharField(
                        db_index=True,
                        max_length=120,
                    ),
                ),
                (
                    "health_check_schedule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="healthcheck_for_%(class)s",
                        to="django_celery_beat.crontabschedule",
                    ),
                ),
                (
                    "update_task",
                    models.OneToOneField(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_for_%(class)s",
                        to="django_celery_beat.periodictask",
                    ),
                ),
                (
                    "update_schedule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_for_%(class)s",
                        to="django_celery_beat.crontabschedule",
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="pythonmodule",
            options={"ordering": ["base_path", "module"]},
        ),
        migrations.AlterUniqueTogether(
            name="pythonmodule",
            unique_together={("module", "base_path")},
        ),
        migrations.CreateModel(
            name="Parameter",
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
                ("name", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("int", "Int"),
                            ("float", "Float"),
                            ("str", "Str"),
                            ("bool", "Bool"),
                            ("list", "List"),
                            ("dict", "Dict"),
                        ],
                        max_length=10,
                    ),
                ),
                ("description", models.TextField(blank=True, default="")),
                ("is_secret", models.BooleanField(db_index=True)),
                ("required", models.BooleanField()),
                (
                    "python_module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="parameters",
                        to="api_app.pythonmodule",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "python_module")},
            },
        ),
    ]
