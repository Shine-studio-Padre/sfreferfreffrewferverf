from django.shortcuts import render, get_object_or_404
from futbokas.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import render
#from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string
def index(request):
    items = Item.objects.all()
    context = {
        'title': 'Dr.Shop',
        'items': items
    }
    return render(request, 'shop/index.html', context)

def show_item(request, item_id):
    item = get_object_or_404(Item, id = item_id)
    return render(request, 'shop/item.html', {'item': item})
def order(request):
    context = {
    }
    return render(request, 'shop/order.html', context)