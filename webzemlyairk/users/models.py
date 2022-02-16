from datetime import datetime
from django.db import models

# Create your models here.
class Person(models.Model):
    full_name = models.TextField('ФИО')
    phone1 = models.CharField('Телефон 1', max_length=12)
    phone2 = models.CharField('Телефон 2', max_length=12, blank=True, null=True)
    email = models.EmailField('Email')
    is_client = models.BooleanField('Клиент?')
    position = models.TextField('Должность', blank=True, null=True)
    role_id = models.IntegerField('Роль', blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    photo = models.ImageField('Фото', upload_to='photos', blank=True, null=True)
    self_registration = models.BooleanField('Регистрация на сайте', blank=True, null=True)
    password = models.CharField('Пароль', max_length=250)
    emp = models.ForeignKey('Person', on_delete=models.CASCADE, blank=True, null=True)
    date_delete = models.DateField('Дата удаления', blank=True, null=True)

    class Meta:
       managed = True
       ordering = ["-id"]

    def __str__(self):
        return self.full_name

    def add_client(client, request):
        client.full_name = request.POST.get("full_name")
        client.phone1 = request.POST.get("phone1")
        client.phone2 = request.POST.get("phone2")
        client.email = request.POST.get("email")
        client.is_client = True
        client.comment = request.POST.get("comment")
        client.self_registration = False
        client.password = request.POST.get("password")
        # client.emp = 

        print(client)
        client.save()
        return client

    def edit_client(client, request, pk):
        client = Person.objects.get(id=pk)
        print(client)
        client.full_name = request.POST.get("full_name")
        client.phone1 = request.POST.get("phone1")
        client.phone2 = request.POST.get("phone2")
        client.email = request.POST.get("email")
        client.comment = request.POST.get("comment")
        if request.POST.get("password") != None:
            client.password = request.POST.get("password")
        client.save()
        return client

    def delete_user(pk):
        user = Person.objects.get(id=pk)
        user.date_delete = datetime.today()
        user.save()
        return True

    def get_clients(self):
        return Person.objects.filter(is_client = True, date_delete = None)
    
###############################    

    def add_emp(emp, request):
        emp.full_name = request.POST.get("full_name")
        emp.phone1 = request.POST.get("phone1")
        emp.phone2 = request.POST.get("phone2")
        emp.email = request.POST.get("email")
        emp.is_client = False
        emp.position = request.POST.get("position")
        emp.role_id = 1
        emp.comment = request.POST.get("comment")
        emp.password = request.POST.get("password")
        emp.photo = request.FILES['photo'].name

        print(emp)
        emp.save()
        return emp

    def edit_emp(emp, request, pk):
        emp = Person.objects.get(id=pk)

        emp.full_name = request.POST.get("full_name")
        emp.phone1 = request.POST.get("phone1")
        emp.phone2 = request.POST.get("phone2")
        emp.email = request.POST.get("email")
        emp.position = request.POST.get("position")
        emp.role_id = 1
        emp.comment = request.POST.get("comment")
        emp.photo = request.POST.get("photo")
        emp.comment = request.POST.get("comment")
        if request.POST.get("password") != None:
            emp.password = request.POST.get("password")
        
        emp.save()
        return emp

    def delete_user(pk):
        user = Person.objects.get(id=pk)
        user.date_delete = datetime.today()
        user.save()
        return True

    def get_emps(self):
        return Person.objects.filter(is_client = False, date_delete = None)
