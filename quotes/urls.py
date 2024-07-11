from django.urls import path
from .views import UserQuoteDetailView, AdminQuoteView

urlpatterns = [
    path('user/quotes/<int:pk>/', UserQuoteDetailView.as_view(), name='user-quote-detail'),
    path('admin/quotes/', AdminQuoteView.as_view(), name='admin-quote-list-create'),
    path('admin/quotes/<int:pk>/', AdminQuoteView.as_view(), name='admin-quote-detail')
]
