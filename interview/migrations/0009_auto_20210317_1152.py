# Generated by Django 3.1.7 on 2021-03-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_auto_20210317_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interview.countryarea'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_id',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='url',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='vfm',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
