# Generated by Django 4.0 on 2022-01-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to='blog_images/'),
        ),
    ]
