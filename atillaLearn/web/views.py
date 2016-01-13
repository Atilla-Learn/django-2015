from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Item
# Create your views here.

def index(request):
    return render_to_response('index.html')

class TalkListView(ListView):

    model = Item
    queryset = Item.objects.filter(type=Item.TALK)
    template_name = 'talks.html'
