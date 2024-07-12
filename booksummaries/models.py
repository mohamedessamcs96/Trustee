from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from ckeditor.fields import RichTextField



class BookSummary(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    #summary = models.TextField()
    summary=RichTextField()
    image = models.ImageField(upload_to='book_images/')  # New field for the book image
    seen_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_summaries', blank=True)  # Track users who have seen the summary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class BookPurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_summary = models.ForeignKey(BookSummary, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(auto_now_add=True)

class BookSummaryAccessLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_summary = models.ForeignKey(BookSummary, on_delete=models.CASCADE)
    access_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def count_monthly_accesses(cls, user):
        one_month_ago = timezone.now() - timedelta(days=30)
        return cls.objects.filter(user=user, access_time__gte=one_month_ago).count()

    @classmethod
    def has_exceeded_monthly_limit(cls, user):
        return cls.count_monthly_accesses(user) >= 3

    @classmethod
    def has_purchased_in_last_year(cls, user, book_summary):
        one_year_ago = timezone.now() - timedelta(days=365)
        return BookPurchase.objects.filter(user=user, book_summary=book_summary, purchase_time__gte=one_year_ago).exists()
