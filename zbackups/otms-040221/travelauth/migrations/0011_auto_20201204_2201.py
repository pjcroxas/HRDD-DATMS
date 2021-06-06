# Generated by Django 3.1.1 on 2020-12-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelauth', '0010_travelrequest_tbl_assigned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='acknowledgement',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='clothing_allowance',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='dsa_day',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='echo',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='echo_seminar',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='endorsement',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='inviting_institute',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='other_expense',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='other_remarks',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='perday',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='pre_travel_expense',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='ptr_dnpt',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='ptr_submitted',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='received',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='released',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='rep_allowance',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='sponsor',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='ta_signed_upload',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='training_report',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='travelrequest_tbl',
            name='year',
        ),
        migrations.AlterField(
            model_name='travelrequest_tbl',
            name='status',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
