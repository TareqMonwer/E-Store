from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Think Python',
                    author='Allen B. Downey',
                    price='20.99')
        
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Think Python')
        self.assertEqual(f'{self.book.author}', 'Allen B. Downey')
        self.assertEqual(f'{self.book.price}', '20.99')

    def test_book_list_view(self):
        resp = self.client.get(reverse('book-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Think Python')
        self.assertTemplateUsed(resp, 'books/book_list.html')
    
    def test_book_detail_view(self):
        resp = self.client.get(self.book.get_absolute_url())
        no_resp = self.client.get('/books/123/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'Think Python')
        self.assertTemplateUsed(resp, 'books/book_detail.html')