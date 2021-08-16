from django.urls import path, include

from . import views
from .views import BooksDetailView, BookSearch

urlpatterns = [
    path('getbooks/', views.get_books, name='read'),
    path('addbooks/', views.add_book, name='create'),
    path('updatebook/<int:book_id>', views.update_book, name='update'),
    path('deletebook/<int:book_id>', views.delete_book, name='delete'),
    path('', views.index, name='home'),
    path('login1/', include('rest_auth.urls'), name='login'),
    path('registration/', include('rest_auth.registration.urls'), name='registr'),
    path('book/<str:id>', BooksDetailView.as_view(), name='detail_book'),
    path('books/', BookSearch.as_view(), name='books')
]
