from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^addArticle/', views.addArticle, name='addArticle'),
    url(r'^editArticle/(?P<title>[a-zA-Z0-9_% ]+)/', views.editArticle, name='editArticle'),
    url(r'^showCat/(?P<id>[0-9]+)/', views.showCat, name='showCat'),
]