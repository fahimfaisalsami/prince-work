# Generated by Django 5.0.6 on 2024-10-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgw_management', '0008_kgwstuffovertime_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeMachineriesExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uom', models.CharField(max_length=50, verbose_name='Unit of Measure')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
