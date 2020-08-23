from django.db import models

# Create your models here.

class Category(models.Model):
    '''Database Model of Category Table '''
    name = models.CharField(max_length=20)


class Post(models.Model):
    '''Database Model of Post Table '''
    title = models.CharField(max_length=255)
    body = models.TextField()
    createdOn = models.DateTimeField(auto_now_add= True)
    lastModified = models.DateTimeField(auto_now= True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    '''Database Model of Comment Table '''
    author = models.CharField(max_length=60)
    body = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('post', on_delete=models.CASCADE)
