from django.db import models
from django.utils import timezone
# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField( default = timezone.now)

    def __str__(self):
        return self.title

# Create your models here.
