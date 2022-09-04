from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    tagname = models.CharField(max_length=50)
    

    def __str__(self):
        return self.tagname

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    tag = models.ManyToManyField(Tag , blank=True)
    thumnail = models.ImageField(default = 'thumnail.jpg' , blank = True , null = True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100 , unique=True , null=True , blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def _get_absolute_url(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug , num)
            num += 1
        return unique_slug
    
    def save(self, *args , **kwargs):
        self.slug = self._get_absolute_url()
        return super().save(*args , **kwargs)