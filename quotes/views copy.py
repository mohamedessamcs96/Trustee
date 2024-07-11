from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Quote
from .serializers import QuoteSerializer

class UserQuoteDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        quote = self.get_object(pk)
        user = request.user

        if quote.seen_by.filter(id=user.id).exists():
            return Response({"detail": "You have already seen this quote."}, status=status.HTTP_403_FORBIDDEN)

        quote.seen_by.add(user)
        quote.save()

        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

# View for admins to manage quotes
class AdminQuoteView(generics.ListCreateAPIView, 
                     generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAdminUser]


# class QuoteView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return BookSummary.objects.get(pk=pk)
#         except BookSummary.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         summary = self.get_object(pk)
#         user = request.user

#         if summary.seen_by.filter(id=user.id).exists():
#             return Response({"detail": "You have already seen this summary."}, status=status.HTTP_403_FORBIDDEN)

#         summary.seen_by.add(user)
#         summary.save()

#         serializer = BookSummarySerializer(summary)
#         return Response(serializer.data)

