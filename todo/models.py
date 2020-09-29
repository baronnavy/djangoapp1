from django.db import models
from django.urls import reverse

# Create your models here.

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    images = models.ImageField(upload_to='')
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY,
        null=True, blank=True, default='normal'
    )
    duedate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})