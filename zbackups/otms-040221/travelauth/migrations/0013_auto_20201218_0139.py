# Generated by Django 3.1.1 on 2020-12-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelauth', '0012_auto_20201209_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrequest_tbl',
            name='office',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
