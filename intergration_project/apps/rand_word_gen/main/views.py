from django.shortcuts import render, redirect
import random, string
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def generate(request):
    if request.method == 'POST':
        request.session['count'] +=1
        request.session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        return redirect('/' )
    else:
        return redirect('/')
