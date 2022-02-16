from django.shortcuts import redirect, render
from .models import Feedback
from .forms import FeedbackForm, ObjectFeedbackForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class FeedbacksView(ListView):
    model = Feedback
    template_name = 'feedbacks/adminFeedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 1

class CheckFeedback(ListView):
    model = Feedback
    template_name = 'feedbacks/adminFeedback.html'
    context_object_name = 'feedbacks'
    
    def post(self, request, pk):
        r = Feedback.check_f(pk)
        return redirect('feedbacks')

class AddFeedback(CreateView):
    model = Feedback
    template_name = 'main/buy.html'
    context_object_name = 'f'
    
    def post(self, request):
        r = Feedback().add(request)
        return redirect('mainpage')
