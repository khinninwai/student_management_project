from django.db import models

# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = [
        ('','Choose gender'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name