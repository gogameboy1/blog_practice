from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^addArticle/', views.addArticle, name='addArticle'),
    url(r'^editArticle/(?P<title>[a-zA-Z0-9_% ]+)/', views.editArticle, name='editArticle'),
    url(r'^showCategory/(?P<category>[a-zA-Z0-9_% ]+)/', views.showCat, name='showCat')
]