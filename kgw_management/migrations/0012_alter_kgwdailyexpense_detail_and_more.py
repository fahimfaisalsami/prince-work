# Generated by Django 5.0.6 on 2024-11-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgw_management', '0011_kctcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kgwdailyexpense',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kgwdailyexpense',
            name='job_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kgwdailyexpense',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kgwdailyexpense',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='kgwdailyexpense',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
