from django.contrib.auth.models import User
from django.db import models
from django.forms import Field
from django.utils import *
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    alias = models.SlugField(verbose_name='Alias категории')
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"
    def __str__(self):
        return 'Категория: %s' % self.name

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена товара')
    image = models.CharField(max_length=255, verbose_name='Изображение')
    text = models.TextField()
    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"
    def __str__(self):
        return 'Товар: %s' % self.name

