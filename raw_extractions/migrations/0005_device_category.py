# Generated by Django 2.1.3 on 2018-11-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_extractions', '0004_remove_device_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='category',
            field=models.ForeignKey(default=1, on_delete='PROTECT', to='raw_extractions.ControllerType', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
