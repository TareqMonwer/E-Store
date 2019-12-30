from django.urls import path

from .views import BookListView, BookDetailView, authorization_required


urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('unauthorized_request/', authorization_required, name='authorization-required'),
]