# Generated by Django 3.1.7 on 2021-03-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_hotelreview_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelreview',
            name='UUID',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
