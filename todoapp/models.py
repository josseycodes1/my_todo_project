from django.db import models

# Define a class called ToDo, which will be a table in the database
class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)  # A True/False field to mark if a task is done

    def __str__(self):
        return self.title 

