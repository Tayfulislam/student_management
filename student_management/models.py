from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    address = models.TextField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

