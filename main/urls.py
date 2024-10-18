from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.report, name='report'),
    path('oil/', views.oil, name='oil'),
    path('oil/delete_oil/<int:id>/', views.delete_oil),
    path('oil/edit_oil/<int:id>/', views.edit_oil),
    path('oil/add_oil/', views.create_oil),
]
