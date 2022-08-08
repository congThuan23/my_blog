from dataclasses import dataclass
from email.policy import default
from enum import auto
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    body = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
