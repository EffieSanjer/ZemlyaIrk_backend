from django.shortcuts import redirect, render
from .models import Person
from feedbacks.models import Comment
from .forms import ClientForm, EmployeeForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

def users(self):
    return redirect('all_clients')
# Create your views here.
class ClientsView(ListView):
    model = Person
    template_name = 'users/adminUsers.html'
    context_object_name = 'clients'
    queryset = Person().get_clients()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        ctx = super(ClientsView, self).get_context_data(**kwargs)
        clients = Person().get_clients()
        
        search_type = 'name'
        search = self.request.GET.get('search', '')
        
        if search != '' and search is not None:
            if self.request.GET.get('search_type') == 'name':
                clients = clients.filter(full_name__icontains = search)
                search_type = 'name'
                ctx['search_type'] = search_type
            
            if self.request.GET.get('search_type') == 'phone':
                clients = clients.filter(phone1__icontains = search)
                search_type = 'phone'
                ctx['search_type'] = search_type
            
            if self.request.GET.get('search_type') == 'email':
                clients = clients.filter(email__icontains = search)
                search_type = 'email'
                ctx['search_type'] = search_type
        
        ctx['clients'] = clients
        ctx['query'] = '&search=' + search + '&search_type=' + search_type
        return ctx

class ClientCard(DetailView):
    model = Person
    template_name = 'users/adminUs.html'
    context_object_name = 'client'

class AddClient(CreateView):
    form_class = ClientForm
    template_name = 'users/adminAddClient.html'
    # offices = Office.get_all_offices()
    context_object_name = 'client'


    def post(self, request):
        form = ClientForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            client = Person()
            client = Person.add_client(client, request)
            # form.save()
        return redirect('all_clients')

    # def get_context_data(self, **kwargs):
    #     ctx = super(AddClient, self).get_context_data(**kwargs)
    #     ctx['offices'] = self.offices
    #     return ctx

class EditClient(UpdateView):
    model = Person
    form_class = ClientForm
    template_name = 'users/adminEditClient.html'
    context_object_name = 'client'

    def post(self, request, pk):
        form = ClientForm(request.POST)
        print(request.POST)
        client = Person()
        
        print(form)
        if form.is_valid():
            client = Person.edit_client(client, request, pk)
            # form.save()
        return redirect('client_item', pk)

class DeleteClient(DeleteView):
    model = Person
    context_object_name = 'client'

    def post(self, request, pk):
        is_delete = Person.delete_user(pk)
        print(is_delete)
        if is_delete:
            return redirect('all_clients')
        return pk

class DeleteComm(DetailView):
    model = Person
    template_name = 'users/adminUs.html'
    context_object_name = 'client'

    def post(self, request, client_id, pk):
        # client = self.kwargs['client_id']
        # print(client)
        # comm = self.kwargs['pk']
        # print(comm)
        
        cm = Comment.delete(pk)
        return redirect('client_item', client_id)

class AddComm(CreateView):
    model = Comment
    template_name = 'users/adminUs.html'
    context_object_name = 'comm'

    def post(self, request, client_id):
        cm = Comment()
        cm = Comment.add_client(cm, request, client_id)
        
        return redirect('client_item', client_id)


##########################

class TeamView(ListView):
    model = Person
    template_name = 'users/adminTeam.html'
    context_object_name = 'emps'
    queryset = Person().get_emps()
    paginate_by = 3

class TeamCard(DetailView):
    model = Person
    template_name = 'users/adminEmp.html'
    context_object_name = 'emp'

class AddEmp(CreateView):
    form_class = EmployeeForm
    template_name = 'users/adminAddUser.html'
    # roles = Office.get_all_offices()
    context_object_name = 'emp'


    def post(self, request):
        form = EmployeeForm(request.POST)
        print(request.POST)
        print(request.FILES['photo'])
        p = FileSystemStorage()
        p.save(request.FILES['photo'].name, request.FILES['photo'])
        print(form)
        if form.is_valid():
            emp = Person()
            emp = Person.add_emp(emp, request)
            # form.save()
        return redirect('all_emps')

    # def get_context_data(self, **kwargs):
    #     ctx = super(AddClient, self).get_context_data(**kwargs)
    #     ctx['offices'] = self.offices
    #     return ctx

class EditEmp(UpdateView):
    model = Person
    form_class = EmployeeForm
    template_name = 'users/adminEditUser.html'
    context_object_name = 'emp'

    def post(self, request, pk):
        form = EmployeeForm(request.POST)
        print(request.POST)
        emp = Person()
        
        print(form)
        if form.is_valid():
            emp = Person.edit_emp(emp, request, pk)
            # form.save()
        return redirect('emp_item', pk)

class DeleteEmp(DeleteView):
    model = Person
    context_object_name = 'emp'

    def post(self, request, pk):
        is_delete = Person.delete_user(pk)
        print(is_delete)
        if is_delete:
            return redirect('all_emps')
        return pk
