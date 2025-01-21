from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field  # Make sure this is the only editor import

class Post(models.Model):
    TOPICS = [
        ('tech', 'Technology'),
        ('personal', 'Personal'),
        ('philosophy', 'Philosophy'),
        ('mentorship', 'Mentorship'),

    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = CKEditor5Field()
    excerpt = models.TextField(max_length=500)
    featured_image = models.ImageField(upload_to='blog_images/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPICS, default='personal')


    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title