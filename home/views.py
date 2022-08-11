from curses.ascii import HT
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def handler404(request, exception):
    return render(request, 'pages/error.html', {'message': exception})

def handler500(request, *args, **argv):
    response = render_to_response('pages/error.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    return render(request, 'pages/register.html',{'form':form})


