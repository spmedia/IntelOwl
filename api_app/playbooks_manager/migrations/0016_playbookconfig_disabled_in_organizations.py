# Generated by Django 4.1.9 on 2023-06-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certego_saas_organization', '0001_initial'),
        ('playbooks_manager', '0015_dns_playbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbookconfig',
            name='disabled_in_organizations',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_disabled', to='certego_saas_organization.organization'),
        ),
    ]