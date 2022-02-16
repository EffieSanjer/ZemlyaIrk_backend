from datetime import datetime
from django.db import models

# Create your models here.
class Message(models.Model):
    user_from = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='user_from')
    user_to = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='user_to')
    theme = models.CharField('Тема', max_length=250, blank=True, null=True)
    message = models.TextField('Сообщение', blank=True, null=True)
    date = models.DateField('Дата', default=datetime.today())
    date_marked_sender = models.DateField('Дата отметки отправителем', blank=True, null=True)
    date_marked_receiver = models.DateField('Дата отметки получателем', blank=True, null=True)
    date_sended = models.DateField('Дата отправки', blank=True, null=True)
    date_delete = models.DateField('Дата удаления', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def add(m, request):
        m.user_from_id = 6
        m.user_to_id = request.POST.get("user_to")
        m.theme = request.POST.get("theme")
        m.message = request.POST.get("message")
        m.date_sended = datetime.today()

        m.save()
        return m
    
    def delete(pk):
        m = Message.objects.get(id=pk)
        m.date_delete = datetime.today()
        m.save()
        return True