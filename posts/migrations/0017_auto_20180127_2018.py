# Generated by Django 2.0.1 on 2018-01-27 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20180127_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 27, 14, 48, 33, 342081, tzinfo=utc)),
        ),
    ]