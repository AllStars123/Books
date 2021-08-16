import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def index(request):
    content = {'message': 'Test'}
    return JsonResponse(content)


# Посмотреть все книги (GET)
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)


# Добавить книгу (POST)
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = Author.objects.get(id=payload['author'])
        book = Book.objects.create(
            title=payload['title'],
            description=payload['description'],
            added_by=user,
            author=author
        )
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Обновить запись (PUT)
@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        book_item = Book.objects.filter(added_by=user, id=book_id)
        book_item.update(**payload)
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Удалить запись по id (DELETE)
@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    user = request.user.id
    try:
        book = Book.objects.get(added_by=user, id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR

                            )


class BooksDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'


class BookSearch(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # filter_backends = [SearchFilter]
    # search_fields = ['title', 'author']
    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.query_params.get('title')
        return qs.filter(title__iexact=title)
