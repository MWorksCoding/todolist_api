from django.db import models
from django.conf import settings
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    
    def time_passed(self):
        now = datetime.now().date()  # Extracting date portion of current datetime
        created_date = self.created_at.date()  # Extracting date portion of created_at
        delta = now - created_date # Calculate the difference
        return delta.days