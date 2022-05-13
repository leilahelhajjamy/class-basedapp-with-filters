from django.db import models
from django.urls import reverse
# Create your models here.



class Student(models.Model):
    firstName= models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = models.FloatField()
    # tell django where it should go after the student is created

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk':self.pk})