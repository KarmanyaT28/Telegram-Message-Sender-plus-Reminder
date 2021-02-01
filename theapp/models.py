from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date,time
from ckeditor.fields import RichTextField




class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)


    def _str_(self):
        return self.title + '   |   ' +str(self.author)

    def get_absolute_url(self):
        # return reverse('details', args=(str(self.id)))
        return reverse('home')


class User(models.Model):
    image = models.ImageField(upload_to="profiles",null=True,blank=True)
    