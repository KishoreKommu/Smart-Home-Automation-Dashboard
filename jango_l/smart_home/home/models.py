from django.db import models

class Device(models.Model):
    DEVICE_TYPES = (
        ('Light', 'Light'),
        ('Fan', 'Fan'),
        ('Sensor', 'Sensor'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPES, default='Other')
    is_on = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {'ON' if self.is_on else 'OFF'}"

    

