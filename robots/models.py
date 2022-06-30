from django.db import models

class Robot(models.Model):
    message = models.CharField(max_length=200)
