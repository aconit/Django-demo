from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import CustomLoginForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.decorators import user_passes_test
from . import forms

@user_passes_test(lambda u: u.isEmployee)
def users_list(request):
    users=User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, 'users/users_list.html', {'users':users})

@user_passes_test(lambda u: u.isEmployee)
def users_edit(request, id):
    if id == 0:
        user = None
    else:
        user = get_object_or_404(User, id=id)

    if request.method == "POST":
        form = forms.EditUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')     
    else:
        if id >0:
            user.password='';
        form = forms.EditUser(instance=user)

    return render(request, 'users/users_edit.html', {'form': form})


@user_passes_test(lambda u: u.isEmployee)
def users_delete(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('users') 
    
    form = forms.EditUser(instance=user)
    return render(request, 'users/users_delete.html', {'form': form})

@login_not_required
def users_login(request):
    if request.method == "POST":     
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user());
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('books') 
    else:
        form =CustomLoginForm()
    return render(request,'users/login.html', {'form':form} )

def users_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('books') 