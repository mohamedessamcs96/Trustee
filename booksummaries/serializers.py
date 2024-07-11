from rest_framework import serializers
from .models import BookSummary

class BookSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSummary
        fields = '__all__'  # or specify individual fields you want to include
