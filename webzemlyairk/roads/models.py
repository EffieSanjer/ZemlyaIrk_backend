from django.db.models import Q
from datetime import datetime
from django.db import models

# Create your models here.

class Locality(models.Model):

    type_dict = [
        (1, 'Населенный пункт'),
        (2, 'Садоводство'),
        (3, 'Коттеджный поселок'),
        (4, 'Местность'),
        (5, 'Тракт')
    ]

    name = models.CharField('Название', max_length=250)
    show_name = models.CharField('Название для показа', max_length=250)
    type = models.IntegerField('Тип', choices=type_dict)
    distance = models.DecimalField('Удаленность', max_digits=6, decimal_places=2)
    description = models.TextField('Описание', null=True, blank=True)
    latitude = models.DecimalField('Широта', max_digits=8, decimal_places=6)
    longitude = models.DecimalField('Долгота', max_digits=8, decimal_places=6)
    photos = models.JSONField('Фотографии', default="{}")
    date_delete = models.DateField('Дата удаления', null=True, blank=True)
    childs = models.ManyToManyField('Locality', through='Family', related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def add(r, request):
        r.name = request.POST.get("name")
        r.show_name = request.POST.get("show_name")
        r.type = request.POST.get("type")
        r.distance = request.POST.get("distance")
        r.description = request.POST.get("description")
        r.latitude = request.POST.get("latitude")
        r.longitude = request.POST.get("longitude")
        r.save()

        if (request.POST.get("parent") != '0'):
            Family().add(request.POST.get("parent"), r.id)
        return r
    
    def edit(r, request, pk):
        r = Locality.objects.get(id=pk)

        r.name = request.POST.get("name")
        r.show_name = request.POST.get("show_name")
        r.type = request.POST.get("type")
        r.distance = request.POST.get("distance")
        r.description = request.POST.get("description")
        r.latitude = request.POST.get("latitude")
        r.longitude = request.POST.get("longitude")

        r.save()
        return r

    def delete(pk):
        r = Locality.objects.get(id=pk)
        r.date_delete = datetime.today()
        r.save()
        return True

    def get_all(self):
        return Locality.objects.filter(date_delete = None)

    def get_roads(self):
        return Locality.objects.filter(type = 5, date_delete = None)

    def get_parents(self):

        return Locality.objects.filter(type = 0, date_delete = None)

    def get_childs(self):
        return Locality.get_all(self).exclude(type = 0)

    # def get_road_parent(self, pk):
    #     l = Locality.objects.get(id=pk)
    #     print(l.parent.all)
    #     print(l.child.all)
    #     return Locality.get_all(self).exclude(type = 0)



class Family(models.Model):
    child = models.ForeignKey('Locality', on_delete=models.PROTECT, related_name='child')
    parent = models.ForeignKey('Locality', on_delete=models.PROTECT, related_name='parent')

    def add(self, p, c):
        f = Family.objects.create(parent_id = p, child_id = c)
        return f
    