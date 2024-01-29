from django.db import models

class TodoListData(models.Model):
    title=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    current_time = models.DateTimeField()
