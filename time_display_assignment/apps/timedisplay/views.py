from django.shortcuts import render, HttpResponse
from datetime import *
# Create your views here.
stamp = datetime.now()
def index(request):
    print stamp
    context = {
    'key': stamp
    }
    return render(request,'timedisplay/index.html', context)
