# Generated by Django 3.1.4 on 2021-01-28 06:13

from django.db import migrations, models
import requestor.validators


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0005_auto_20201209_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestor',
            name='last_file',
            field=models.FileField(blank=True, null=True, upload_to='signed_nomination/%Y/%m/%d/', validators=[requestor.validators.validate_file_extension]),
        ),
    ]
