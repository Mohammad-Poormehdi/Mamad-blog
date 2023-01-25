from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    def __str__(self):
        return self.title

class PostComment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='uploads')
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    comment = models.ManyToManyField(PostComment, blank=True)