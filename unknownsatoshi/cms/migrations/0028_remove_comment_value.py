# Generated by Django 3.2.4 on 2022-10-19 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0027_auto_20221019_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='value',
        ),
    ]
