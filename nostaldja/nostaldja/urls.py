# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),
    path('decade/<int:pk>',views.decade_detail, name='decade_detail'),
    path('fad/<int:pk>',views.fad_detail, name='fad_detail'),

]