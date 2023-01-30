# Generated by Django 4.1.4 on 2023-01-30 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_alter_bank_joining_date_alter_upload_invoice_in_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approve_invoice',
            old_name='approve',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='approve_invoice',
            old_name='emp_code',
            new_name='in_amount',
        ),
        migrations.RenameField(
            model_name='approve_invoice',
            old_name='loan_amount',
            new_name='in_num',
        ),
        migrations.RenameField(
            model_name='deny_invoice',
            old_name='approve',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='deny_invoice',
            old_name='emp_code',
            new_name='in_amount',
        ),
        migrations.RenameField(
            model_name='deny_invoice',
            old_name='loan_amount',
            new_name='in_num',
        ),
        migrations.RenameField(
            model_name='deny_invoice',
            old_name='phnum',
            new_name='sup_code',
        ),
        migrations.RenameField(
            model_name='request_invoice',
            old_name='client_code',
            new_name='in_amount',
        ),
        migrations.RenameField(
            model_name='request_invoice',
            old_name='loan_amount',
            new_name='in_num',
        ),
        migrations.RenameField(
            model_name='view_invoice',
            old_name='approve',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='view_invoice',
            old_name='emp_code',
            new_name='in_amount',
        ),
        migrations.RenameField(
            model_name='view_invoice',
            old_name='loan_amount',
            new_name='in_num',
        ),
        migrations.RenameField(
            model_name='view_invoice',
            old_name='phnum',
            new_name='sup_code',
        ),
        migrations.RemoveField(
            model_name='approve_invoice',
            name='name',
        ),
        migrations.RemoveField(
            model_name='approve_invoice',
            name='phnum',
        ),
        migrations.RemoveField(
            model_name='deny_invoice',
            name='name',
        ),
        migrations.RemoveField(
            model_name='request_invoice',
            name='name',
        ),
        migrations.RemoveField(
            model_name='request_invoice',
            name='phnum',
        ),
        migrations.RemoveField(
            model_name='view_invoice',
            name='name',
        ),
        migrations.AddField(
            model_name='approve_invoice',
            name='in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 967953, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='approve_invoice',
            name='sup_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deny_invoice',
            name='in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 967953, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='request_invoice',
            name='currency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='request_invoice',
            name='in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 966957, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='request_invoice',
            name='sup_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='view_invoice',
            name='in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 967953, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='joining_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 965960, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='upload_invoice',
            name='in_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 13, 36, 41, 967953, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
