# Generated by Django 4.1.2 on 2022-10-15 16:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_incidentreport_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='immediateAction',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='incidentLocation',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='initialSeverity',
            field=models.CharField(blank=True, choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Fatal', 'Fatal')], default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='subIncidentTypes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Environmental Incident', 'Environmental Incident'), ('Injury/Illness', 'Injury/Illness'), ('Property Damage', 'Property Damage'), ('Vehicle', 'Vehicle')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='suspectedCause',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='location',
            field=models.CharField(blank=True, choices=[('Corporate Headoffice', 'Corporate Headoffice'), ('Operations Department', 'Operations Department'), ('Work Station', 'Work Station'), ('Marketing Division', 'Marketing Division')], default='Corporate Headoffice', max_length=30, null=True),
        ),
    ]
