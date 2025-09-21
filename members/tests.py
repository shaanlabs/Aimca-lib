
from django.test import TestCase, Client
from django.urls import reverse
from .models import Member, BookLoan
from books.models import Book
from django.utils import timezone

class MemberModelTest(TestCase):
	def setUp(self):
		self.member = Member.objects.create(
			name="Test Member",
			email="test@example.com",
			phone="1234567890",
			address="123 Test St",
			is_active=True
		)

	def test_member_str(self):
		self.assertEqual(str(self.member), "Test Member")

	def test_member_ordering(self):
		member2 = Member.objects.create(
			name="Another Member",
			email="another@example.com",
			phone="0987654321",
			address="456 Test Ave",
			is_active=True
		)
		members = Member.objects.all()
		self.assertEqual(list(members), sorted(list(members), key=lambda m: m.name))

class BookLoanModelTest(TestCase):
	def setUp(self):
		self.book = Book.objects.create(
			title="Test Book",
			author="Test Author",
			isbn="1234567890123",
			publication_year=2020,
			quantity=5,
			available_quantity=5
		)
		self.member = Member.objects.create(
			name="Test Member",
			email="test@example.com",
			phone="1234567890",
			address="123 Test St",
			is_active=True
		)
		self.loan = BookLoan.objects.create(
			book=self.book,
			member=self.member,
			due_date=timezone.now() + timezone.timedelta(days=7),
			status='borrowed'
		)

	def test_bookloan_str(self):
		self.assertEqual(str(self.loan), f"{self.book.title} - {self.member.name}")

	def test_is_overdue(self):
		self.assertFalse(self.loan.is_overdue())
		self.loan.due_date = timezone.now() - timezone.timedelta(days=1)
		self.loan.save()
		self.assertTrue(self.loan.is_overdue())

class MemberViewsTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.member = Member.objects.create(
			name="Test Member",
			email="test@example.com",
			phone="1234567890",
			address="123 Test St",
			is_active=True
		)

	def test_member_list_view(self):
		response = self.client.get(reverse('member_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Test Member")
