from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Post title')
    message = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.name