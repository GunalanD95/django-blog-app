# Generated by Django 4.0 on 2022-01-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_blog_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to='blog_app/'),
        ),
    ]