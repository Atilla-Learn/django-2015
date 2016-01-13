from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item
# Create your views here.

def index(request):
    context = {
        'num_trainings': Item.objects.filter(type=Item.TRAINING).count(),
        'num_conferences': Item.objects.filter(type=Item.CONFERENCE).count(),
        'num_talks': Item.objects.filter(type=Item.TALK).count(),
    }
    return render(request, 'index.html', context=context)

class CountItems(object):

    def get_context_data(self, **kwargs):
        context = super(CountItems, self).get_context_data(**kwargs)
        context.update({
            'num_trainings': Item.objects.filter(type=Item.TRAINING).count(),
            'num_conferences': Item.objects.filter(type=Item.CONFERENCE).count(),
            'num_talks': Item.objects.filter(type=Item.TALK).count(),
        })
        return context

class TrainingListView(CountItems, ListView):

    model = Item
    queryset = Item.objects.filter(type=Item.TRAINING)
    template_name = 'trainings.html'

class TalkListView(CountItems, ListView):

    model = Item
    queryset = Item.objects.filter(type=Item.TALK)
    template_name = 'talks.html'

class ConferenceListView(CountItems, ListView):

    model = Item
    queryset = Item.objects.filter(type=Item.CONFERENCE)
    template_name = 'conferences.html'

class ItemDetailView(CountItems, DetailView):

    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'
