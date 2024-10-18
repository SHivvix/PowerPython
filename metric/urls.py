from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index_meter'),
    path('value/', views.value, name='value'),
    path('value/value_add/', views.value_add, name='value_add'),
    path('value/delete_value/<int:id>', views.delete_value, name='delete_value'),
    path('value/edit_value/<int:id>', views.edit_value, name='edit_value')
]
