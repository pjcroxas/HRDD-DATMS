# Generated by Django 3.1.4 on 2021-02-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0009_auto_20210204_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestor',
            name='taketimestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
