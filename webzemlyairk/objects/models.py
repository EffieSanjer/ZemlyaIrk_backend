
from django.db import models
from datetime import datetime
from users.models import Person

from django.db.models.expressions import F

# Create your models here.

class Object(models.Model):
    type_dict = [
        (1, 'Земельный участок'),
        (2, 'Бизнес-объект'),
        (3, 'Дом'),
        (4, 'Дача'),
        (5, 'Коттедж'),
        (6, 'Готовый бизнес'),
        (7, 'Промышленная база'),
        (8, 'Таунхауз')
    ]
    otherobj_dist = [
        (1,'Дом'),
        (2,'Гараж'),
        (3,'Теплица'),
        (4,'Баня'),
        (5,'Колодец')
    ]
    
    status_dist = [
        (1,'Показывается'),
        (2,'Скрыт'),
        (3,'Продан')
    ]
    posession_dist = [
        (1,'Собственность'),
        (2,'Не собственность'),
        (3,'Садоводческая книжка'),
        (4,'Аренда'),
        (5,'Пожизненно наследуемое владение'),
        (6,'Членская книжка')
    ]

    purpose_dist = [
        (1,'Для индивидуального жилищного строительства'),
        (2,'Для организации садоводства и жилищного строительства'),
        (3,'Для ведения личного подсобного хозяйства'),
        (4,'Земли водного и лесного фонда'),
        (5,'Земли особо охраняемых территорий'),
        (6,'Земли промышленности, транспорта, энергетики'),
        (7,'Для ведения крестьянско-фермерского хозяйства'),
        (8,'Для организации садоводства и дачного строительства')
    ]

    type = models.IntegerField('Тип объекта', choices=type_dict)
    seller = models.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='seller')
    locality = models.ForeignKey('roads.Locality', on_delete=models.PROTECT, related_name='locality')
    parent = models.ForeignKey('roads.Locality', on_delete=models.PROTECT, related_name='country')
    distance = models.DecimalField('Удаленность', max_digits=6, decimal_places=2)
    address = models.CharField('Адрес', max_length=250)
    area = models.DecimalField('Площадь', max_digits=6, decimal_places=2)
    object_area = models.DecimalField('Площадь объекта', max_digits=6, decimal_places=2, blank=True, null=True)
    other_objects = models.IntegerField('Другие объекты', choices=otherobj_dist, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    date_update = models.DateField('Дата обновления')
    cadast_num = models.CharField('Кадастровый номер', max_length=20)
    rating = models.IntegerField('Рейтинг')
    status = models.IntegerField('Статус', choices=status_dist)
    posession = models.IntegerField('Владение', choices=posession_dist, default=1)
    purpose = models.IntegerField('Назначение', choices=purpose_dist, default=1)
    source = models.CharField('Ресурс', max_length=250, blank=True, null=True)
    link = models.TextField('Ссылка на обзор', blank=True, null=True)
    resp_emp = models.ForeignKey('users.Person', on_delete=models.PROTECT, blank=True, null=True, related_name='resp_emp')
    cost = models.DecimalField('Стоимость', max_digits=10, decimal_places=3)
    comission = models.DecimalField('Комиссия', max_digits=4, decimal_places=2)
    price_conditions = models.TextField('Условия цены', blank=True, null=True)
    good_price = models.BooleanField('Хорошая цена')
    bargain = models.BooleanField('Торг')
    invest_attract = models.BooleanField('Инвестиционная привлекательность')
    photos = models.JSONField('Фотографии', default="{}", blank=True, null=True)
    charact = models.JSONField('Харктеристики', default="{}", blank=True, null=True)
    infrast = models.JSONField('Инфраструктура', default="{}", blank=True, null=True)
    latitude = models.DecimalField('Широта', max_digits=8, decimal_places=6)
    longitude = models.DecimalField('Долгота', max_digits=8, decimal_places=6)
    date_delete = models.DateField('Дата удалениия', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='Объект'
        verbose_name_plural='Объекты'
        ordering = ['-date_update']
        #managed = False

    def add(o, request):
        o.type = request.POST.get("type")
        o.seller_id = request.POST.get("seller")
        o.locality_id = request.POST.get("locality")
        o.parent_id = request.POST.get("parent")
        o.distance = request.POST.get("distance")
        o.address = request.POST.get("address")
        o.area = request.POST.get("area")
        o.object_area = request.POST.get("object_area")
        o.other_objects = request.POST.get("other_objects")
        o.description = request.POST.get("description")
        o.date_update = datetime.today()
        o.cadast_num = request.POST.get("cadast_num")
        o.rating = request.POST.get("rating")
        o.status = request.POST.get("status")
        o.posession = request.POST.get("posession")
        o.purpose = request.POST.get("purpose")
        o.source = request.POST.get("source")
        o.link = request.POST.get("link")
        o.resp_emp = request.POST.get("resp_emp")
        o.cost = request.POST.get("cost")
        o.comission = request.POST.get("comission")
        o.price_conditions = request.POST.get("price_conditions")
        if (request.POST.get("good_price") == 'on'):
            o.good_price = True
        else:
            o.good_price = False
            
        if ( request.POST.get("bargain") == 'on'):
            o.bargain = True
        else:
            o.bargain = False
        
        if (request.POST.get("invest_attract")):
            o.invest_attract = True
        else:
            o.invest_attract = False
            
        o.latitude = request.POST.get("latitude")
        o.longitude = request.POST.get("longitude")

        o.save()
        return o
    
    def edit(o, request, pk):
        o = Object.objects.get(id=pk)

        o.seller_id = request.POST.get("seller")
        # o.locality_id = request.POST.get("locality")
        o.parent_id = request.POST.get("parent")
        o.distance = request.POST.get("distance")
        o.address = request.POST.get("address")
        o.area = request.POST.get("area")
        o.object_area = request.POST.get("object_area")
        o.other_objects = request.POST.get("other_objects")
        o.description = request.POST.get("description")
        o.date_update = datetime.today()
        o.cadast_num = request.POST.get("cadast_num")
        o.rating = request.POST.get("rating")
        o.status = request.POST.get("status")
        o.posession = request.POST.get("posession")
        o.purpose = request.POST.get("purpose")
        o.source = request.POST.get("source")
        o.link = request.POST.get("link")
        o.resp_emp = request.POST.get("resp_emp")
        o.cost = request.POST.get("cost")
        o.comission = request.POST.get("comission")
        o.price_conditions = request.POST.get("price_conditions")
        if (request.POST.get("good_price") == 'on'):
            o.good_price = True
        else:
            o.good_price = False
            
        if ( request.POST.get("bargain") == 'on'):
            o.bargain = True
        else:
            o.bargain = False
        
        if (request.POST.get("invest_attract")):
            o.invest_attract = True
        else:
            o.invest_attract = False
            
        # o.latitude = request.POST.get("latitude")
        # o.longitude = request.POST.get("longitude")

        o.save()
        return o

    def delete(pk):
        o = Object.objects.get(id=pk)
        o.date_delete = datetime.today()
        o.save()
        return True

    def get_client_obj(pk):
        p = Person.objects.get(id=pk)
        return p.seller.all()
    
    def compare(self, request):
        p = Object.objects.filter(id__in=request.POST.getlist('comp'))
        # for x in request.POST.getlist('comp'):

        return p