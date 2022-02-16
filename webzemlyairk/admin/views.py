from users.models import Person
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'emp' : Person.objects.get(id=6)
    }
    template = 'admin/admin.html'
    return render(request, template, context)