# Generated by Django 2.1.3 on 2018-11-21 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw_extractions', '0003_auto_20181121_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='category',
        ),
    ]
