from django.db import models
import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Job(models.Model):
    job_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.job_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Email(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    email_text = models.CharField(max_length=2000)
   

    def __str__(self):
        return self.email_text