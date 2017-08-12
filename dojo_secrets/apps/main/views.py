from django.shortcuts import render,redirect
from django.db.models import Count
from .models import *
import bcrypt
# Create your views here.
def index(request):

    return render(request, 'main/index.html')

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
    return  redirect('/error')

def success(request):
    id = request.session['user_id']
    user = User.objects.filter(id=id).first()
    context = {
        'user': user,
        'secrets': Secret.objects.all(),
        'like': 'Like'
    }
    return render(request, 'main/success.html', context)

def log_in(request):
    login = User.objects.log_in(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/success')
    return redirect('/error')

def error(request):
    return render(request, 'main/error.html')

def create_secret(request):
    Secret.objects.create(
        user = User.objects.filter(id=request.session['user_id']).first(),
        secret = request.POST.get('secret'),
        likes = 0
        )
    return redirect('/success')

def popsecret(request):
    context = {
        'popsecrets': Secret.objects.all()
    }
    return render(request, 'main/most_popular_secrets.html', context)

def like(request, id):
    likes = User.objects.filter(id__likes=id).count()
    Secret.objects.filter(id=id).update(likes=likes)
    return redirect('/success')
