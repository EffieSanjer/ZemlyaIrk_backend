
from django.shortcuts import render, redirect
from django.views.generic import ListView
from objects.models import Object
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contact.html')

def compare(request):
    return render(request, 'main/comparison.html')
    
def buy(request):
    return render(request, 'main/buy.html')

def sell(request):
    return render(request, 'main/sell.html')

def search(request):
    return render(request, 'main/search.html')

class Compare(ListView):
    model = Object
    template_name = 'main/comparison.html'
    context_object_name = 'objects'     
    o = Object()
    
    def get_context_data(self, **kwargs):
        ctx = super(Compare, self).get_context_data(**kwargs)
        ctx['o'] = self.o
        return ctx


    def post (self, request):
        r = Object().compare(request)
        print(r)
        queryset = super(Compare, self).get_queryset()
        print(queryset)
        return redirect('compare')
  
