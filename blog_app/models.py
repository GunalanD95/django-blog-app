from django.db import models
from django.db.models import fields

import datetime
from datetime import date

# Create your models here.


class Blog(models.Model):
    title = fields.CharField(max_length=100)
    body = fields.CharField(max_length=1000000)
    created_at = models.DateField(default=date.today)
    blog_image = models.ImageField(upload_to='blog_app/', blank=True)

    def __str__(self):
        return f"{self.title}"

