# Generated by Django 4.0 on 2022-01-07 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_blog_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at']},
        ),
    ]
