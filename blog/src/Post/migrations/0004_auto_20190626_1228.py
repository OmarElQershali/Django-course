# Generated by Django 2.2.2 on 2019-06-26 19:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20190626_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 19, 28, 17, 365356, tzinfo=utc)),
        ),
    ]