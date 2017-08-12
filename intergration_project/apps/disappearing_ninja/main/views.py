from django.shortcuts import render,redirect

# Create your views here.
def index(request):

    return render(request, 'main/index.html')



def show(request, word):
    context = {
        'word': word,
    }

    return render(request, 'main/show.html', context)
