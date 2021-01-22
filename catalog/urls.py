from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed-books/',
         permission_required('BookInstance.Can_view_all_borrowed_books')(views.LoanedBooksByAllUserListView.as_view()),
         name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', permission_required('catalog.can_add_author')(views.AuthorCreate.as_view()),
         name='author-create'),
    path('author/<int:pk>/update/', permission_required('catalog.can_add_author')(views.AuthorUpdate.as_view()),
         name='author-update'),
    path('author/<int:pk>/delete/', permission_required('catalog.can_add_author')(views.AuthorDelete.as_view()),
         name='author-delete'),

]
