# Generated by Django 3.1.1 on 2020-12-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestor',
            name='reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
