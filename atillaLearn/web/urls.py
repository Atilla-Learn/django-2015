from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trainings$', views.TrainingListView.as_view(), name='trainings'),
    url(r'^talks$', views.TalkListView.as_view(), name='talks'),
    url(r'^conferences$', views.ConferenceListView.as_view(), name='conferences'),
    url(r'^(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
