from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, subject: {self.subject}"
