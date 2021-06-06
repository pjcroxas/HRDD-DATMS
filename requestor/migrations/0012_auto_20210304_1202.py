# Generated by Django 3.1.4 on 2021-03-04 04:02

from django.db import migrations, models
import requestor.validators


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0011_requestor_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestor',
            name='attended_training',
            field=models.FileField(blank=True, null=True, upload_to='a_t/%Y/%m/%d/', validators=[requestor.validators.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='requestor',
            name='pending_case',
            field=models.FileField(blank=True, null=True, upload_to='pending_case/%Y/%m/%d/', validators=[requestor.validators.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='requestor',
            name='pending_task',
            field=models.FileField(blank=True, null=True, upload_to='pending_tasks/%Y/%m/%d/', validators=[requestor.validators.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='requestor',
            name='service_record',
            field=models.FileField(blank=True, null=True, upload_to='s_r/%Y/%m/%d/', validators=[requestor.validators.validate_file_extension]),
        ),
    ]
