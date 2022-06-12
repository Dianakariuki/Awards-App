from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidato

# Create your models here.

class Projects(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/')
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    date=models.DateField(auto_now=True)
    screen1=models.ImageField(upload_to='screenshot/',blank=True)
    screen2=models.ImageField(upload_to='screenshot/',blank=True)
    
    
    
    class Meta:
        ordering=['-name']

    def __str__(self):
        self.name
    @classmethod
    def search_project(cls,word):
        searched=cls.objects.filter(name__icontains=word)
        return searched


class Profile(models.Model):
    profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    class Meta:
        ordering=['-profile']