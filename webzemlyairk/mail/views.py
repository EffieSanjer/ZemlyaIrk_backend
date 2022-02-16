from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class AdminMess(ListView):
    model = Message
    template_name = 'mail/adminMess.html'
    context_object_name = 'messages'
    paginate_by = 1

# class AdminRoad(DetailView):
#     model = Locality
#     template_name = 'roads/adminOneRoad.html'
#     context_object_name = 'road'

class AddMess(CreateView):
    form_class = MessageForm
    template_name = 'mail/adminMess.html'
    context_object_name = 'mess'


    def post(self, request):
        form = MessageForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            m = Message()
            m = Message.add(m, request)
            # form.save()
        return redirect('messages')



# class DeleteRoad(DeleteView):
#     model = Locality
#     template_name = 'roads/adminOneRoad.html'
#     # fields = ['name']

#     def post(self, request, pk):
#         is_delete = Locality.delete(pk)
#         print(is_delete)
#         if is_delete:
#             return redirect('localities')
#         return pk
