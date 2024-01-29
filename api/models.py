from django.db import models

class Todo(models.Model):
    todo_titles = models.CharField(max_length=255)
    todo_descriptions = models.TextField()

    def __str__(self):
        return self.todo_titles
    