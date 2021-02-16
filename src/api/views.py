from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
