from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta, datetime
from .models import Book
from .forms import BookForm
from members.models import BookLoan, Member
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def dashboard(request):
    # Get current time
    current_time = timezone.now()
    
    # Get recent loans (last 5)
    recent_loans = BookLoan.objects.filter(status='borrowed').order_by('-borrowed_date')[:5]
    
    # Get management loans (for faculty)
    management_loans = BookLoan.objects.filter(status='borrowed').order_by('-borrowed_date')[:5]
    
    # Get overdue count
    overdue_count = BookLoan.objects.filter(status='borrowed', due_date__lt=current_time).count()
    
    # Get available books count
    available_books = Book.objects.filter(available_quantity__gt=0).count()
    
    # Get issued books count
    issued_books = BookLoan.objects.filter(status='borrowed').count()
    
    # Calculate percentages for analytics
    total_books = Book.objects.count()
    issued_percentage = round((issued_books / total_books * 100) if total_books > 0 else 0, 1)
    new_books_percentage = 73  # Placeholder
    overdue_percentage = round((overdue_count / total_books * 100) if total_books > 0 else 0, 1)
    sold_percentage = 65  # Placeholder
    
    # Get library alerts (books due today)
    library_alerts = BookLoan.objects.filter(
        status='borrowed',
        due_date__date=current_time.date()
    )[:5]
    
    context = {
        'current_time': current_time,
        'recent_loans': recent_loans,
        'management_loans': management_loans,
        'overdue_count': overdue_count,
        'available_books': available_books,
        'issued_books': issued_books,
        'issued_percentage': issued_percentage,
        'new_books_percentage': new_books_percentage,
        'overdue_percentage': overdue_percentage,
        'sold_percentage': sold_percentage,
        'library_alerts': library_alerts,
    }
    
    return render(request, 'dashboard.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def is_librarian(user):
    return user.is_superuser or user.groups.filter(name='Librarian').exists()

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.available_quantity = book.quantity
            book.save()
            messages.success(request, f'Book "{book.title}" added successfully!')
            return redirect('book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def lend_book(request):
    # Display form and handle lending a book to a member
    if request.method == 'POST':
        member_id = request.POST.get('member')
        book_id = request.POST.get('book')
        due_date_str = request.POST.get('due_date')

        try:
            member = get_object_or_404(Member, id=member_id)
            book = get_object_or_404(Book, id=book_id)

            if book.available_quantity <= 0:
                messages.error(request, 'Selected book is not available.')
                return redirect('lend_book')

            # Parse due_date (YYYY-MM-DD from input type=date) and make it aware
            if due_date_str:
                due_date_naive = datetime.strptime(due_date_str, '%Y-%m-%d')
                # Set due time to end of the selected day for convenience
                due_date_naive = due_date_naive.replace(hour=23, minute=59, second=59)
                if timezone.is_naive(due_date_naive):
                    due_date = timezone.make_aware(due_date_naive, timezone.get_current_timezone())
                else:
                    due_date = due_date_naive
            else:
                # Default due date: 14 days from now
                due_date = timezone.now() + timedelta(days=14)

            # Create loan
            BookLoan.objects.create(
                book=book,
                member=member,
                due_date=due_date,
                status='borrowed',
            )

            # Decrement availability
            book.available_quantity -= 1
            book.save()

            messages.success(request, f'"{book.title}" lent to {member.name}.')
            return redirect('lent_books')

        except Exception as e:
            messages.error(request, f'Error lending book: {str(e)}')
            return redirect('lend_book')

    # GET: show form with active members and available books
    members = Member.objects.filter(is_active=True)
    available_books = Book.objects.filter(available_quantity__gt=0).order_by('title')
    return render(request, 'books/lend_book.html', {
        'members': members,
        'available_books': available_books,
    })

@login_required
@user_passes_test(is_librarian)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            updated_book = form.save(commit=False)
            active_loans = BookLoan.objects.filter(book=book, status='borrowed').count()
            if updated_book.quantity < active_loans:
                messages.warning(request, f"Quantity set below active loans ({active_loans}). Adjusted to match.")
                updated_book.quantity = active_loans
            updated_book.available_quantity = max(0, updated_book.quantity - active_loans)
            updated_book.save()
            messages.success(request, f'Book "{updated_book.title}" updated successfully!')
            return redirect('book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def lent_books(request):
    lent_books = BookLoan.objects.filter(status='borrowed').order_by('-borrowed_date')
    return render(request, 'books/lent_books.html', {'lent_books': lent_books})

def return_book(request):
    returned_loans = BookLoan.objects.filter(status='returned').order_by('-returned_date')
    return render(request, 'books/return_book.html', {'returned_loans': returned_loans})

def overdue_books(request):
    current_time = timezone.now()
    overdue_books = BookLoan.objects.filter(
        status='borrowed',
        due_date__lt=current_time
    ).order_by('due_date')
    
    # Calculate days overdue and fine for each loan
    for loan in overdue_books:
        loan.days_overdue = (current_time.date() - loan.due_date.date()).days
        loan.fine_amount = loan.days_overdue * 50  # ₹50 per day
    
    return render(request, 'books/overdue_books.html', {'overdue_books': overdue_books})

def process_return(request, loan_id):
    if request.method == 'POST':
        loan = get_object_or_404(BookLoan, id=loan_id)
        loan.status = 'returned'
        loan.returned_date = timezone.now()
        loan.save()
        
        # Update book available quantity
        book = loan.book
        book.available_quantity += 1
        book.save()
        
        messages.success(request, f'Book "{loan.book.title}" returned successfully!')
    
    return redirect('return_book')

def about_us(request):
    return render(request, 'about_us.html')

def book_api(request):
    books = Book.objects.all()
    data = []
    for book in books:
        data.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'available_quantity': book.available_quantity,
        })
    return JsonResponse({'books': data})
