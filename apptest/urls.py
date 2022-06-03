from django.urls import path
from . import  views

app_name = 'apptest'

urlpatterns = [
    path('', views.index, name='index'),
    path('test01/', views.test01, name='test01'),
    path('test02/', views.test02, name='test02'),
    path('testargopath/', views.testargopath, name='testargopath'),
    path('argopath/<platformname>', views.testargopath, name='testargopath'),
    path('getTemAndSalt/<platformnumber>/<cyclenumber>', views.getTemAndSalt, name='getTemAndSalt'),
]