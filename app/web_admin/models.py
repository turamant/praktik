from django.contrib.auth.models import User
from django.db import models


class New(models.Model):
    '''New - сущность новость'''

    class Meta:
        db_table = 'news'
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ("-date",)

    date = models.DateField(verbose_name='Дата(d.m.Y)')
    subject = models.CharField(verbose_name='Заголовок новости', max_length=256)
    content = models.TextField(verbose_name='Содержание новости')
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
