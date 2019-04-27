from django.db import models
from django.conf import settings
from django.utils import timezone


class Case(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    case_number = models.CharField(max_length = 20)
    description = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)



    def publish(self):
        self.created_date= timezone.now()
        self.save

    def __str__(self):
        return self.case_number
