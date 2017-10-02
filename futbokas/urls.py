
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings
from futbokas import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order/$', views.order, name='item'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.show_item, name='item'),
]

