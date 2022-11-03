from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('Comment', on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)