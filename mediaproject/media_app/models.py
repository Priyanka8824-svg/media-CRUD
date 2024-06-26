from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER=[
        ('Male','male'),
        ('Female','female'),
        ('Others','others')
    ]

    pid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER)
    profile_pic = models.ImageField(upload_to='profiles/')
    address = models.TextField()
    city = models.CharField(max_length=20)