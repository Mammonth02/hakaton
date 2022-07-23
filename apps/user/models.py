from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.direction.models import Direction

# Create your models here.


class User(AbstractUser):
    CHOICES = (
        ('developer', 'Разработчик'),
        ('customer', 'Заказчик'),
    )

    group = models.CharField(choices=CHOICES, verbose_name='тип пользователя', max_length=100)

    # developer = models.BooleanField(default=False)
    # customer = models.BooleanField(default=False)

    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Аватарка')
    phone = models.IntegerField(validators=[MinValueValidator(12), MaxValueValidator(12)], null=True, blank=True, verbose_name='Телефон')
    direction = models.ManyToManyField(Direction, blank=True, null=True, verbose_name='Направления')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Mесто жительства')

    
    
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name= 'Пользователь'
    
    def __str__(self):
        return f'{self.username} {self.id}'

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user.customer = True

#     class Meta:
#         verbose_name_plural = 'Заказчики'
#         verbose_name = 'Заказчик'



# class Developer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user.developer = True

#     direction = models.ManyToManyField(Direction, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         verbose_name_plural = 'Разработчики'
#         verbose_name= 'Разработчик'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.group == 'developer':
#             Developer.objects.create(user=instance)
#         elif instance.group == 'customer':
#             Customer.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.group == 'developer':
#         instance.developer.save()
#     elif instance.group == 'customer':
#         instance.customer.save()






