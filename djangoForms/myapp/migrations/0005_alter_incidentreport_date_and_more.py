# Generated by Django 4.1.2 on 2022-10-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_incidentreport_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='incidentDepartment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='location',
            field=models.CharField(choices=[('Corporate Headoffice', 'Corporate Headoffice'), ('Operations Department', 'Operations Department'), ('Work Station', 'Work Station'), ('Marketing Division', 'Marketing Division')], default='Corporate Headoffice', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
