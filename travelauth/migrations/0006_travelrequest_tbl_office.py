# Generated by Django 3.1.1 on 2020-11-26 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelauth', '0005_travel_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelrequest_tbl',
            name='office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travelauth.travel_office'),
        ),
    ]
