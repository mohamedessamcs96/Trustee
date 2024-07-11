from django.contrib import admin
from .models import BookSummary,BookSummaryAccessLog
# Register your models here.
admin.site.register(BookSummary)
admin.site.register(BookSummaryAccessLog)