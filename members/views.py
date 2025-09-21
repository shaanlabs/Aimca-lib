from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Member, BookLoan

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        try:
            member = Member.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address
            )
            messages.success(request, f'Member "{member.name}" added successfully!')
            return redirect('member_list')
        except Exception as e:
            messages.error(request, f'Error adding member: {str(e)}')
    
    return redirect('member_list')

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.email = request.POST.get('email')
        member.phone = request.POST.get('phone')
        member.address = request.POST.get('address')
        member.save()
        
        messages.success(request, f'Member "{member.name}" updated successfully!')
        return redirect('member_list')
    
    return render(request, 'members/edit_member.html', {'member': member})

def delete_member(request, pk):
        member = get_object_or_404(Member, pk=pk)
        member_name = member.name
        member.delete()
        messages.success(request, f'Member "{member_name}" deleted successfully!')
        return redirect('member_list')
