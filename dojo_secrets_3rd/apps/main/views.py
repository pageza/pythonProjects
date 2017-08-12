from django.shortcuts import render,redirect
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
    return  redirect('/')

def log_in(request):
    login = User.objects.log_in(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/success')
    return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')

def success(request):
    id = request.session['user_id']
    user = User.objects.filter(id=id).first()
    context = {
        'user': user,
        'secrets': Secret.objects.all().order_by('-created_at')[:10],
        'likes': Like.objects.all()
    }
    return render(request, 'main/success.html', context)

def create_secret(request):
    Secret.objects.create(
        user = User.objects.filter(id=request.session['user_id']).first(),
        secret = request.POST.get('secret'),
        )
    return redirect('/success')

def like(request, id):
    user = User.objects.filter(id=request.session['user_id']).first()
    print user
    print  Like.objects.all().first().liker
    print  Like.objects.all().first().liked
    secret = Secret.objects.filter(id=id).first()
    print id
    print secret
    like = Like(liker=user,liked=secret)
    print like
    like.save()
    return redirect('/success')

def popsecret(request):
    return render(request, 'main/most_popular_secrets.html')

def delete(request, id):
    Secret.objects.filter(id=id).delete()
    return redirect('/success')
