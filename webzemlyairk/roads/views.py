from django.shortcuts import render, redirect
from .models import Locality
from .forms import LocalityForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class Roads(ListView):
    model = Locality
    template_name = 'roads/mapRoads.html'
    context_object_name = 'roads'
    queryset = Locality().get_roads()


class Road_Card(DetailView):
    model = Locality
    template_name = 'roads/road.html'
    context_object_name = 'road'

###############
class AdminRoads(ListView):
    model = Locality
    template_name = 'roads/adminRoads.html'
    context_object_name = 'roads'
    queryset = Locality().get_all()
    paginate_by = 7

class AdminRoad(DetailView):
    model = Locality
    template_name = 'roads/adminOneRoad.html'
    context_object_name = 'road'

class AddRoad(CreateView):
    form_class = LocalityForm
    template_name = 'roads/adminAddRoad.html'
    r = Locality()
    context_object_name = 'road'


    def post(self, request):
        form = LocalityForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            r = Locality()
            r = Locality.add(r, request)
            # form.save()
        return redirect('localities')

    def get_context_data(self, **kwargs):
        ctx = super(AddRoad, self).get_context_data(**kwargs)
        ctx['r'] = self.r
        ctx['parents'] = self.r.get_parents()
        ctx['childs'] = self.r.get_childs()
        return ctx

class EditRoad(UpdateView):
    model = Locality
    form_class = LocalityForm
    template_name = 'roads/adminEditRoad.html'
    context_object_name = 'road'
    r = Locality()

    def post(self, request, pk):
        form = LocalityForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            r = Locality()
            r = Locality.edit(r, request, pk)
            # form.save()
        return redirect('loc', pk)
    
    def get_context_data(self, **kwargs):
        ctx = super(EditRoad, self).get_context_data(**kwargs)
        ctx['r'] = self.r
        ctx['childs'] = self.r.get_childs()
        # ctx['road_parent'] = self.r.get_road_parent(self.kwargs['pk'])
        return ctx

class DeleteRoad(DeleteView):
    model = Locality
    template_name = 'roads/adminOneRoad.html'
    # fields = ['name']

    def post(self, request, pk):
        is_delete = Locality.delete(pk)
        print(is_delete)
        if is_delete:
            return redirect('localities')
        return pk
