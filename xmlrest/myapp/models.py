from django.db import models

# Create your models here.
class student(models.Model):
    stid = models.IntegerField()
    name = models.CharField( max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name