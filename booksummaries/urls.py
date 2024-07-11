from django.urls import path
from .views import BookSummaryListCreate,BookSummaryDetail

urlpatterns = [
    path('book-summaries/', BookSummaryListCreate.as_view(), name='book-summary-list-create'),
    path('book-summaries/<int:pk>/', BookSummaryDetail.as_view(), name='book-summary-detail'),
    # path('book-summary/access/<int:book_summary_id>/', access_book_summary, name='access-book-summary'),

]
