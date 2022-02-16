from roads.models import Locality
from django.shortcuts import render, redirect
from .models import Object
from feedbacks.models import Comment
from .forms import ObjectForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

def objects(self):
    return redirect('country')

class Place_Card(DetailView):
    model = Object
    template_name = 'objects/place.html'
    context_object_name = 'place'


class ObjectView(ListView):
    model = Object
    template_name = 'objects/countryPlaces.html'
    context_object_name = 'obj'
    # queryset = Object.objects.all()
    # obj = Object.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx = super(ObjectView, self).get_context_data(**kwargs)
        # ctx['obj'] = self.obj
        obj = Object.objects.filter(date_delete = None)

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            obj = obj.order_by(sort)
        
        show = self.request.GET.get('show', 3)
        paginator = Paginator(obj, show)


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
            'obj' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

####################

class AdminObjectView(ListView):
    model = Object
    template_name = 'objects/adminObj.html'
    context_object_name = 'objects'
    
    def get_context_data(self, **kwargs):
        ctx = super(AdminObjectView, self).get_context_data(**kwargs)
        objects = Object.objects.filter(date_delete = None)

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            objects = objects.order_by(sort)
        
        show = self.request.GET.get('show', 3)
        paginator = Paginator(objects, show)

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
            'objects' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

        
class AdminPlaceView(DetailView):
    model = Object
    template_name = 'objects/adminObject.html'
    context_object_name = 'place'

class AddObj(CreateView):
    form_class = ObjectForm
    template_name = 'objects/adminAddPlace.html'
    o = Object()
    # offices = Office.get_all_offices()
    context_object_name = 'obj'


    def post(self, request):
        form = ObjectForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            o = Object()
            o = Object.add(o, request)
            # form.save()
        return redirect('objects')

    def get_context_data(self, **kwargs):
        ctx = super(AddObj, self).get_context_data(**kwargs)
        ctx['o'] = self.o
        ctx['childs'] = Locality().get_childs()
        ctx['parents'] = Locality().get_parents()
        return ctx

class EditObj(UpdateView):
    model = Object
    form_class = ObjectForm
    template_name = 'objects/adminEditPlace.html'
    context_object_name = 'obj'
    o = Object()
    # offices = Office.get_all_offices()

    def post(self, request, pk):
        form = ObjectForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            o = Object()
            o = Object.edit(o, request, pk)
            # form.save()
        return redirect('place', pk)
    
    def get_context_data(self, **kwargs):
        ctx = super(EditObj, self).get_context_data(**kwargs)
        ctx['o'] = self.o
        ctx['childs'] = Locality().get_childs()
        ctx['parents'] = Locality().get_parents()
        return ctx

class DeleteObj(DeleteView):
    model = Object
    template_name = 'objects/adminObj.html'
    # fields = ['name']

    def post(self, request, pk):
        is_delete = Object.delete(pk)
        print(is_delete)
        if is_delete:
            return redirect('objects')
        return pk

class DeleteComm(DetailView):
    model = Object
    template_name = 'users/adminObject.html'
    context_object_name = 'place'

    def post(self, request, obj_id, pk):
        cm = Comment.delete(pk)
        return redirect('place', obj_id)

class AddComm(CreateView):
    model = Comment
    template_name = 'users/adminObject.html'
    context_object_name = 'comm'

    def post(self, request, obj_id):
        cm = Comment()
        cm = Comment.add_object(cm, request, obj_id)
        
        return redirect('place', obj_id)

class ClientObjectView(ListView):
    model = Object
    template_name = 'objects/adminObj.html'
    context_object_name = 'objects'
    
    def get_context_data(self, **kwargs):
        ctx = super(ClientObjectView, self).get_context_data(**kwargs)
        objects = Object.get_client_obj(self.kwargs['pk'])

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            objects = objects.order_by(sort)

        show = self.request.GET.get('show', 3)
        paginator = Paginator(objects, show)

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
            'objects' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx

################

class FavouriteView(ListView):
    model = Object
    template_name = 'objects/personalLike.html'
    context_object_name = 'obj'
    # queryset = Object.objects.all()
    # obj = Object.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx = super(FavouriteView, self).get_context_data(**kwargs)
        # ctx['obj'] = self.obj
        obj = Object.objects.filter(date_delete = None)

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            obj = obj.order_by(sort)
        
        show = self.request.GET.get('show', 3)
        paginator = Paginator(obj, show)


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
            'obj' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx
class MyObjectsView(ListView):
    model = Object
    template_name = 'objects/personalMySales.html'
    context_object_name = 'obj'
    # queryset = Object.objects.all()
    # obj = Object.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx = super(MyObjectsView, self).get_context_data(**kwargs)
        # ctx['obj'] = self.obj
        obj = Object.objects.filter(date_delete = None)

        #sorting
        sort = self.request.GET.get('sort', '')
        if sort != '':
            obj = obj.order_by(sort)
        
        show = self.request.GET.get('show', 3)
        paginator = Paginator(obj, show)


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
            'obj' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }

        print(ctx)
        return ctx
