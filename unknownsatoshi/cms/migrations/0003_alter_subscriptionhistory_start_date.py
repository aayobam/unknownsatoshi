# Generated by Django 3.2.9 on 2021-12-16 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_subscriptionhistory_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionhistory',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 16, 14, 17, 29, 492432)),
        ),
    ]
