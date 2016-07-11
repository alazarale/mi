from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='image/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('agri:detail', args=[
            self.created.year,
            self.created.strftime('%m'),
            self.created.strftime('%d'),
            self.slug,
        ])

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent']

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_commented')
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    commented = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message

class Product(models.Model):
    STATUS = (('publish', 'Publish'), ('cancel', 'Cancel'))

    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='product/image/')
    description = models.TextField(max_length='1000')
    price = models.FloatField()
    quantity = models.CharField(max_length=50)
    slug = models.SlugField(unique_for_month=True)
    status = models.CharField(max_length=7, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agri:description', args=[
            self.created.strftime('%m'),
            self.created.strftime('%d'),
            self.slug,
        ])








