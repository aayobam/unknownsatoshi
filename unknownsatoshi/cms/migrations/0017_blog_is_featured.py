# Generated by Django 3.1.8 on 2021-11-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20211118_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
