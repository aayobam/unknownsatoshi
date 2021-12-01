# Generated by Django 3.2.9 on 2021-11-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='product_image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='plan',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='cms',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='cms_images/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='course_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='product_images/'),
        ),
    ]