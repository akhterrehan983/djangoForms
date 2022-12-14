# Generated by Django 4.1.2 on 2022-10-15 16:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_incidentreport_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='subIncidentTypes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Environmental Incident', 'Environmental Incident'), ('Injury/Illness', 'Injury/Illness'), ('Property Damage', 'Property Damage'), ('Vehicle', 'Vehicle')], max_length=30, null=True),
        ),
    ]
