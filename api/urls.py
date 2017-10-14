from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/', views.index,name='data'),
    url(r'^notice/', views.notice,name='notice'),
    url(r'^teaminfo/', views.teaminfo,name='teaminfo'),
　　 url(r'^flag/',views.flag,name='flag')
]

