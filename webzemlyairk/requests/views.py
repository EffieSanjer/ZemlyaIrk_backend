from feedbacks.models import Comment
from django.core.paginator import Paginator
from .models import Office, Request, Members
from django.shortcuts import render, redirect
from .forms import RequestForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class RequestView(ListView):
    model = Request
    template_name = 'requests/adminRequests.html'
    context_object_name = 'req'
    
    def get_context_data(self, **kwargs):
        ctx = super(RequestView, self).get_context_data(**kwargs)
        req = Request.objects.all()

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            req = req.order_by(sort)

        #pagination
        show = self.request.GET.get('show', 3)
        paginator = Paginator(req, show)
        
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''

        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx = {
            "show" : int(show),
            "sort" : sort,
            'req' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx
        
class MyRequestView(ListView):
    model = Request
    template_name = 'requests/adminRequests.html'
    context_object_name = 'req'
    
    def get_context_data(self, **kwargs):
        ctx = super(MyRequestView, self).get_context_data(**kwargs)
        req = Request.get_my_orders(6)

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            req = req.order_by(sort)

        show = self.request.GET.get('show', 3)
        paginator = Paginator(req, show)

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''

        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx = {
            "show" : int(show),
            "sort" : sort,
            'req' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

class ClientRequestView(ListView):
    model = Request
    template_name = 'requests/adminRequests.html'
    context_object_name = 'req'
    
    def get_context_data(self, **kwargs):
        ctx = super(ClientRequestView, self).get_context_data(**kwargs)
        req = Request.get_client_orders(self.kwargs['pk'])

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            req = req.order_by(sort)

        show = self.request.GET.get('show', 3)
        paginator = Paginator(req, show)

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''

        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx = {
            "show" : int(show),
            "sort" : sort,
            'req' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

class EmpRequestView(ListView):
    model = Request
    template_name = 'requests/adminRequests.html'
    context_object_name = 'req'
    
    def get_context_data(self, **kwargs):
        ctx = super(EmpRequestView, self).get_context_data(**kwargs)
        req = Request.get_my_orders(self.kwargs['pk'])

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            req = req.order_by(sort)

        show = self.request.GET.get('show', 3)
        paginator = Paginator(req, show)

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''

        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx = {
            "show" : int(show),
            "sort" : sort,
            'req' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

class AddReq(CreateView):
    form_class = RequestForm
    template_name = 'requests/adminAddReq.html'
    req = Request()
    offices = Office.get_all_offices()
    context_object_name = 'req'


    def post(self, request):
        form = RequestForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            order = Request()
            order = Request.add(order, request)
            # form.save()
        return redirect('all_requests')

    def get_context_data(self, **kwargs):
        ctx = super(AddReq, self).get_context_data(**kwargs)
        ctx['req'] = self.req
        ctx['offices'] = self.offices
        return ctx

    # def get_success_url(self):
    #     return reverse('offerta_create',args=(self.object.id,))

class Order_Card(DetailView):
    model = Request
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'

class EditReq(UpdateView):
    model = Request
    form_class = RequestForm
    template_name = 'requests/adminEditReq.html'
    context_object_name = 'order'
    offices = Office.get_all_offices()
    # fields = ['name']

    # def get_initial(self):
    #     initial = super().get_initial()
    #     print(self.request)
    #     print(initial)
    #     initial['name'] = self.request.name
    #     return initial

    def post(self, request, pk):
        form = RequestForm(request.POST)
        print(request.POST)
        order = Request()
        
        print(form)
        if form.is_valid():
            order = Request.edit(order, request, pk)
            # form.save()
        return redirect('order_item', pk)

    def get_context_data(self, **kwargs):
        ctx = super(EditReq, self).get_context_data(**kwargs)
        ctx['offices'] = self.offices
        return ctx

class DeleteReq(DeleteView):
    model = Request
    form_class = RequestForm
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'
    # fields = ['name']

    # def get_initial(self):
    #     initial = super().get_initial()
    #     print(self.request)
    #     print(initial)
    #     initial['name'] = self.request.name
    #     return initial

    def post(self, request, pk):
        form = RequestForm(request.POST)
        print(request.POST)
        print(pk)
        #order = Request()
        is_delete = Request.delete_order(pk)
        print(is_delete)
        if is_delete:
            return redirect('all_requests')
        return pk
        # form.save()

class FinishReq(DetailView):
    model = Request
    template_name = 'requests/adminReqFinish.html'
    context_object_name = 'order'

    def post(self, request, pk):
        r = Request.finish_order(pk)
        return redirect('order_item', pk)

class DeleteComm(DetailView):
    model = Request
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'

    def post(self, request, order_id, pk):
        cm = Comment.delete(pk)
        return redirect('order_item', order_id)

class AddComm(CreateView):
    model = Comment
    template_name = 'requests/adminReq.html'
    context_object_name = 'comm'

    def post(self, request, order_id):
        cm = Comment()
        cm = Comment.add_order(cm, request, order_id)
        
        return redirect('order_item', order_id)

class DeleteMember(DetailView):
    model = Request
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'

    def post(self, request, order_id, pk):
        m = Members.delete_mem(order_id, pk)
        return redirect('order_item', order_id)

class StopReq(DetailView):
    model = Request
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'

    def post(self, request, pk):
        r = Request.stop_order(pk)
        return redirect('order_item', pk)

class ContReq(DetailView):
    model = Request
    template_name = 'requests/adminReq.html'
    context_object_name = 'order'

    def post(self, request, pk):
        r = Request.cont_order(pk)
        return redirect('order_item', pk)