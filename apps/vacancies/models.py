from turtle import title
from django.db import models
from django.core.validators import MinValueValidator

from apps.direction.models import Direction
from apps.user.models import User
# Create your models here.

class Vacancies(models.Model):
    CHOICES = (
        (True, 'Договорная'),
        (False, 'Не договорная'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик', null=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField( verbose_name='Описание')
    price = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True, verbose_name='Оплата')
    company = models.CharField(max_length=100, null=True, blank=True, verbose_name='Компания(не обязательно)')
    contract = models.BooleanField(choices=CHOICES, verbose_name='Цена')
    direction = models.ManyToManyField(Direction, blank=True, null=True, verbose_name='Направления')
    time_creat = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name= 'Вакансия'
    
    def __str__(self):
        return f'{self.user}'

