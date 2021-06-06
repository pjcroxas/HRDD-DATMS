# Generated by Django 3.1.1 on 2020-12-03 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelauth', '0009_remove_travelrequest_tbl_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelrequest_tbl',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='travelassigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
