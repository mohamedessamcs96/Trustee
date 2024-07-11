from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BookSummary, BookSummaryAccessLog
from .serializers import BookSummarySerializer
from .permissions import IsAdminOrReadOnly
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

class BookSummaryListCreate(APIView):
    # permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request):
        summaries = BookSummary.objects.all()
        serializer = BookSummarySerializer(summaries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookSummaryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return BookSummary.objects.get(pk=pk)
        except BookSummary.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        summary = self.get_object(pk)
        user = request.user

        # Check if user has purchased in the last year or exceeded monthly limit
        if not BookSummaryAccessLog.has_purchased_in_last_year(user, summary) and BookSummaryAccessLog.has_exceeded_monthly_limit(user):
            return Response({"detail": "You have exceeded the limit of 3 book summaries per month."}, status=status.HTTP_403_FORBIDDEN)

        # Log the access
        BookSummaryAccessLog.objects.create(user=user, book_summary=summary)

        # Serialize and return the book summary
        serializer = BookSummarySerializer(summary)
        return Response(serializer.data)

@login_required
def access_book_summary(request, book_summary_id):
    book_summary = get_object_or_404(BookSummary, id=book_summary_id)
    
    if not BookSummaryAccessLog.has_purchased_in_last_year(request.user, book_summary) and BookSummaryAccessLog.has_exceeded_monthly_limit(request.user):
        return HttpResponseForbidden("You have exceeded the limit of 3 book summaries per month.")
    
    # Log the access
    BookSummaryAccessLog.objects.create(user=request.user, book_summary=book_summary)
    
    # Render the book summary
    return render(request, 'book_summary_detail.html', {'book_summary': book_summary})
