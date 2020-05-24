from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leadtime = models.IntegerField(null=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.title
