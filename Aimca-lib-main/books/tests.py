
from django.test import TestCase, Client
from django.urls import reverse
from .models import Book

class BookModelTest(TestCase):
	def setUp(self):
		self.book = Book.objects.create(
			title="Test Book",
			author="Test Author",
			isbn="1234567890123",
			publication_year=2020,
			quantity=5,
			available_quantity=5
		)

	def test_book_str(self):
		self.assertEqual(str(self.book), "Test Book by Test Author")

	def test_book_ordering(self):
		book2 = Book.objects.create(
			title="Another Book",
			author="Author 2",
			isbn="1234567890124",
			publication_year=2021,
			quantity=2,
			available_quantity=2
		)
		books = Book.objects.all()
		self.assertEqual(list(books), sorted(list(books), key=lambda b: b.title))

class BookViewsTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.book = Book.objects.create(
			title="Test Book",
			author="Test Author",
			isbn="1234567890123",
			publication_year=2020,
			quantity=5,
			available_quantity=5
		)

	def test_book_list_view(self):
		response = self.client.get(reverse('book_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Test Book")

	def test_add_book_view(self):
		response = self.client.post(reverse('add_book'), {
			'title': 'New Book',
			'author': 'New Author',
			'isbn': '1234567890999',
			'publication_year': 2022,
			'quantity': 3
		})
		self.assertEqual(response.status_code, 302)  # Redirect after success
		self.assertTrue(Book.objects.filter(title='New Book').exists())

	def test_overdue_books_view(self):
		response = self.client.get(reverse('overdue_books'))
		self.assertEqual(response.status_code, 200)
