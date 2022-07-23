from django.db import models

# Create your models here.

class Direction(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Направления'
        verbose_name= 'Направление'
    
    def __str__(self):
        return f'{self.title}'