from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book


def authorization_required(request):
    return render(request, 'unauthorized.html')

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    # for multiple permissions
    permission_required = ('books.standard_pack',)
    
    def handle_no_permission(self):
        ''' AccessMixin's method overriden '''
        return redirect('authorization-required')
