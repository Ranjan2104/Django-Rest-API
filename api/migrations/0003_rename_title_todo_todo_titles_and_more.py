# Generated by Django 5.0.1 on 2024-01-21 16:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_todo_description_todo_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='todo_titles',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_descriptions',
            field=models.TextField(default='hello'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]