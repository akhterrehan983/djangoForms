# Generated by Django 4.1.2 on 2022-10-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_incidentreport_subincidenttypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.userform'),
        ),
    ]
