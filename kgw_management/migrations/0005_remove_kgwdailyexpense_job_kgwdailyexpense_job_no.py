# Generated by Django 5.0.6 on 2024-10-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgw_management', '0004_remove_kgwjobexpenses_job_kgwjobexpenses_job_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kgwdailyexpense',
            name='job',
        ),
        migrations.AddField(
            model_name='kgwdailyexpense',
            name='job_no',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
