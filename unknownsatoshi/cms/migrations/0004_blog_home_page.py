# Generated by Django 3.2.9 on 2021-12-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_productcategory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='home_page',
            field=models.BooleanField(default=False),
        ),
    ]
