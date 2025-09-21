from django.db import models
from django.utils import timezone
from books.models import Book

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    membership_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class BookLoan(models.Model):
    LOAN_STATUS = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=LOAN_STATUS, default='borrowed')
    
    def __str__(self):
        return f"{self.book.title} - {self.member.name}"
    
    def is_overdue(self):
        if self.status == 'returned':
            return False
        return timezone.now() > self.due_date
    
    class Meta:
        ordering = ['-borrowed_date']
