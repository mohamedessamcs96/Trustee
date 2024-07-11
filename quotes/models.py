from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    seen_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_quote', blank=True)  # Track users who have seen the summary
    
    def __str__(self):
        return f'{self.author}: "{self.text}"'




# class Quotes(models.Model):
#     author = models.CharField(max_length=255)
#     body = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='quotes_images/')  # New field for the book image
#     seen_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_summaries', blank=True)  # Track users who have seen the summary
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body

