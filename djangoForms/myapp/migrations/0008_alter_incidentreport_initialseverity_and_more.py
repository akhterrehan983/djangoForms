# Generated by Django 4.1.2 on 2022-10-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_incidentreport_immediateaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='initialSeverity',
            field=models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Fatal', 'Fatal')], default='Mild', max_length=30),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='location',
            field=models.CharField(choices=[('Corporate Headoffice', 'Corporate Headoffice'), ('Operations Department', 'Operations Department'), ('Work Station', 'Work Station'), ('Marketing Division', 'Marketing Division')], default='Corporate Headoffice', max_length=30),
        ),
    ]