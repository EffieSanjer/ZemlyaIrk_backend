from users.models import Person
from django.db import models
from datetime import date, datetime


# Create your models here.
class Request(models.Model):

    dict_urgency = [
        (1, 'Обычная'),
        (2, 'Срочная')
    ]
    dict_status = [
        (1, 'Активна'),
        (2, 'Приостановлена'),
        (3, 'Завершена')
    ]
    # dict_forsale = [
    #     (1, 'На продажу'),
    #     (2, 'На покупку')
    # ]
    dict_progress = [
        (10, 'Заявка оформлена'),
        (20, 'Ведется подбор объектов'),
        (40, 'Согласование с клиентом'),
        (60, 'Согласование с продавцом'),
        (80, 'Оформление документов'),
        (100, 'Заявка завершена')
    ]
    dict_type = [
        (1, 'Замельный участок'),
        (2, 'Дача'),
        (3, 'Коттедж'),
        (4, 'Дом'),
        (5, 'Бизнес-объект'),
        (6, 'Таунхауз')
    ]

    name = models.CharField('Название', max_length=250)
    type = models.IntegerField('Тип объекта', choices=dict_type, default=1)
    seller = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='sellers', blank=True, null=True, default="")
    customer = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='customers', blank=True, null=True, default="")
    object = models.ForeignKey('objects.Object', on_delete=models.PROTECT, related_name='objs', blank=True, null=True, default="")
    date_start = models.DateField('Дата начала', default=date.today())
    date_end = models.DateField('Дата окончания')
    office = models.ForeignKey('Office', on_delete=models.PROTECT, related_name='office', blank=True, null=True, default="")
    description = models.TextField('Описание', blank=True)
    for_sale = models.BooleanField('На продажу')
    status = models.IntegerField('Статус', choices=dict_status, default=1)
    progress = models.IntegerField('Прогресс', choices=dict_progress, default=10)
    urgency = models.IntegerField('Срочность', choices=dict_urgency, default=1)
    date_signed = models.DateField('Дата подписания договора', null=True)
    date_payment = models.DateField('Дата оплаты', null=True)
    date_frs = models.DateField('Дата сдачи документов в ФРС', null=True)
    date_payment_us = models.DateField('Дата оплаты "ЗемляИрк"', null=True)
    # test = models.IntegerField('Test', max_length=250, choices=dict_urgency, default=1, null=True)
    members = models.ManyToManyField('users.Person', through='Members')
    # test = models.JSONField('TEST', null=True)

    class Meta:
        # managed=True
        ordering = ["-id"]

    # def __init__(self):
    #     pass

    def add(order, request):
        order.name = request.POST.get("name")
        # order.date_start = self.date_start
        order.seller_id = request.POST.get("seller")
        order.customer_id = request.POST.get("customer")
        order.object_id = request.POST.get("object")
        order.office_id = request.POST.get("office")
        order.date_end = request.POST.get("date_end")
        order.description = request.POST.get("description")
        order.for_sale = request.POST.get("for_sale")
        order.status = request.POST.get("status")
        # order.progress = 10
        order.urgency = request.POST.get("urgency")
        order.type = request.POST.get("type")
        # order.test = request.POST.get("test")

        print(order)
        print(order.name)
        # Request.objects.create(name = "name", type = "type", date_end = "date_end")
        order.save()
        return order

    def get_absolute_url(self):
        return f'/requests/{self.id}'

    def edit(order, request, pk):
        order = Request.objects.get(id=pk)
        print(order)
        order.name = request.POST.get("name")
        # order.date_start = self.date_start
        order.seller_id = request.POST.get("seller")
        order.customer_id = request.POST.get("customer")
        order.office_id = request.POST.get("office")
        order.object_id = request.POST.get("object")
        order.date_end = request.POST.get("date_end")
        order.description = request.POST.get("description")
        # order.for_sale = request.POST.get("for_sale")
        order.status = request.POST.get("status")
        # order.progress = 10
        order.urgency = request.POST.get("urgency")
        # order.type = request.POST.get("type")
        if request.POST.get("date_signed") != '':
            order.date_signed = request.POST.get("date_signed")
        if request.POST.get("date_payment") != '':
            order.date_payment = request.POST.get("date_payment")
        if request.POST.get("date_frs") != '':
            order.date_frs = request.POST.get("date_frs")
        if request.POST.get("date_payment_us") != '':
            order.date_payment_us = request.POST.get("date_payment_us")

        order.save()
        return order

    def delete_order(pk):
        order = Request.objects.get(id=pk)
        order.delete()
        return True
    
    def stop_order(pk):
        order = Request.objects.get(id=pk)
        print(order)
        order.status = 2
        order.save()
        return True
    
    def cont_order(pk):
        order = Request.objects.get(id=pk)
        print(order)
        order.status = 1
        order.save()
        return True

    def finish_order(pk):
        order = Request.objects.get(id=pk)
        print(order)
        order.status = 3
        order.progress = 100
        order.save()
        return True
    
    def get_my_orders(pk):
        p = Person.objects.get(id=pk)
        return p.request_set.all()
    
    def get_client_orders(pk):
        p = Person.objects.get(id=pk)
        return p.customers.all()

class Members(models.Model):
    employer = models.ForeignKey('users.Person', on_delete=models.DO_NOTHING, related_name='employer')
    order = models.ForeignKey('requests.Request', on_delete=models.DO_NOTHING, related_name='request')
    date_add = models.DateField('Дата добавления', default=date.today())

    class Meta:
        # managed=True
        ordering = ["-id"]

    def delete_mem(order_id, emp_id):
        m = Members.objects.filter(employer_id = emp_id, order_id=order_id)
        m.delete()
        return True


class Office(models.Model):
    name = models.CharField('Название', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    manager = models.ForeignKey('users.Person', on_delete=models.DO_NOTHING, related_name='manager')
    boss = models.ForeignKey('users.Person', on_delete=models.DO_NOTHING, related_name='boss')
    phone = models.CharField('Телефон', max_length=12)
    date_delete = models.DateField('Дата удаления', blank=True, null=True)

    class Meta:
        # managed=True
        ordering = ["name"]

    def get_all_offices():
        return Office.objects.filter(date_delete = None)