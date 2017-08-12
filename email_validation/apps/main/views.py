from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib import messages
from .models import *

import re
message = ''
# Create your views here.
def index(request):
    context = {
        'emails': Email.objects.all(),
        'message': message
    }
    return render(request, 'main/index.html', context)

def submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if len(email) > 5:
            if re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", email):
                emails = Email(email=email)
                emails.save()

        else:
            print "<h1>Email is not Valid!</h1>"
    return redirect('/')
