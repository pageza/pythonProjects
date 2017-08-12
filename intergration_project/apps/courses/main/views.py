from django.shortcuts import render,redirect
from .models import Course
# Create your views here.
def index(request):

    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'main/index.html', context)

def addcourse(request):
        if request.method == 'POST':
            course = Course(name=request.POST.get('name'),description=request.POST.get('comment'))
            course.save()
            return redirect('/')

def destroy(request, id):
    context = {
        'id': id,
        'courses': Course.objects.all(),
        # 'description': Course.objects.description.get(id=id),
    }
    return render(request, 'main/destroy.html', context)

def delete(request,id):
    context ={
    'id' : id
    }
    if request.method == 'POST':
        pass
