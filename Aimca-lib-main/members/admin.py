from django.contrib import admin
from .models import Member, BookLoan

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'membership_date', 'is_active')
    list_filter = ('is_active', 'membership_date')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('membership_date',)

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrowed_date', 'due_date', 'status')
    list_filter = ('status', 'borrowed_date', 'due_date')
    search_fields = ('book__title', 'member__name')
    readonly_fields = ('borrowed_date',)
