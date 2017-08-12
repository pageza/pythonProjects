from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):

    context = {

    }
    return render(request, 'main/index.html', context)
def create_user(request):
    #validate and create UserManager
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name= request.POST.get('name'),
            email= request.POST.get('email'),
            password= bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
        )
        request.session['user_id']= user.id
        return redirect('/success')
    return  redirect('/')

def success(request):
    return render(request, 'main/books.html')

def log_in(request):
    login = User.objects.log_in(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/success')
    return redirect('/')
