from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item
# Create your views here.

def index(request):
    return render_to_response('index.html')

class TalkListView(ListView):

    model = Item
    queryset = Item.objects.filter(type=Item.TALK)
    template_name = 'talks.html'

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'
