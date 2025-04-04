from django.db import models
# Create your models here.

class SystemHealth(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    disk_usage = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - CPU: {self.cpu_usage}%"
