from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect('home')
    else:
        form = UserCreationForm()
    data = {'form':form}
    return render(request,'registration/register.html',data)


def logout_user(request):
    logout(request)
    return render(request,'registration/logout.html')


def login_user(request):
    return render(request,'registration/loasfdasdfasfasfasf1.html')