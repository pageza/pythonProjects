from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    locations = [
        'Dallas',
        'San Francisco',
        'Seattle'
    ]
    languages = [
        'python',
        'php',
        'javascript'
    ]
    context = {
        'locations': locations,
        'languages': languages,
    }
    return render(request, 'main/index.html', context)

def surveys(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['language'] = request.POST.get('language')
        request.session['location'] = request.POST.get('location')
        request.session['comment'] = request.POST.get('comment')
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    return render(request, 'main/success.html')
