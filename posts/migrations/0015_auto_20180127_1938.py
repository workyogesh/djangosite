# Generated by Django 2.0.1 on 2018-01-27 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20180126_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='largePhoto',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 27, 14, 8, 21, 627664, tzinfo=utc)),
        ),
    ]