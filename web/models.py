from django.db import models


class Task(models.Model):
    task = models.CharField(max_length = 1024)
    day = models.CharField(max_length = 1024)
    
    def __str__(self):
        return self.task