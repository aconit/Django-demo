from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from . import forms

def books_list(request):
    books=Book.objects.all()
    return render(request, 'books/books_list.html',{'books':books})

@user_passes_test(lambda u: u.isEmployee)
def books_edit(request, id):
    if id == 0:
        book = None
    else:
        book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = forms.EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books') 
    
    else:
        form = forms.EditBook(instance=book)
        
    return render(request, 'books/books_edit.html', {'form': form})


@user_passes_test(lambda u: u.isEmployee)
def books_delete(request, id):
    book = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('books') 
    
    form = forms.EditBook(instance=book)
    return render(request, 'books/books_delete.html', {'form': form})
