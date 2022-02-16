from datetime import datetime
from django.core.checks import messages
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Feedback(models.Model):
    name = models.TextField('Имя')
    email_phone = models.CharField('Телефон/email', max_length=250)
    date = models.DateField('Дата добавления')
    message = models.TextField('Сообщение', blank=True, null=True)
    for_sale = models.BooleanField('На продажу', blank=True, null=True)
    object_id = models.IntegerField('Объект', blank=True, null=True)
    date_marked = models.DateField('Дата отметки важного', blank=True, null=True)
    date_checked = models.DateField('Дата обработки', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def add(f, request):
        f.name = request.POST.get("name")
        f.email_phone = request.POST.get("email_phone")
        f.date = datetime.today()
        f.message = request.POST.get("message")
        f.for_sale = request.POST.get("for_sale")
        f.object_id = request.POST.get("object_id")

        print(f)
        f.save()
        return f

    def delete(pk):
        user = Feedback.objects.get(id=pk)
        user.delete()
        return True

    def check_f(pk):
        f = Feedback.objects.get(id=pk)
        
        f.date_checked = datetime.today()
        f.save()
        return True

class Comment(models.Model):
    emp = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='emp_comm')
    date = models.DateField('Дата', default=datetime.today())
    message = models.TextField('Сообщение')
    client = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='client_comm', blank=True, null=True)
    object = models.ForeignKey('objects.Object', on_delete=models.PROTECT, related_name='object_comm', blank=True, null=True)
    order = models.ForeignKey('requests.Request', on_delete=models.PROTECT, related_name='order_comm', blank=True, null=True)
    date_delete = models.DateField('Дата удаления', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def add_client(cm, request, cl):
        cm.emp_id = 6
        cm.message = request.POST.get('message')
        cm.client_id = cl
        cm.save()
        return cm

    def add_order(cm, request, cl):
        cm.emp_id = 6
        cm.message = request.POST.get('message')
        cm.order_id = cl
        cm.save()
        return cm
 
    def add_object(cm, request, cl):
        cm.emp_id = 6
        cm.message = request.POST.get('message')
        cm.object_id = cl
        cm.save()
        return cm

    def delete(comm):
        c = Comment.objects.filter(id=comm)
        # print(c.message)
        # Comment.objects.delete(c)
        # c.date_delete = datetime.today()
        c.delete()
        return True
