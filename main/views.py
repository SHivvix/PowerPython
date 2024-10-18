from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import *

# Create your views here.

#Главная страница
def index(request):
    return render(request, 'main/index.html')

#Страница с отчетами
def report(request):
    return render(request, 'main/reports.html')

#Страница счетчиков
def meter(request):
    return render(request, 'main/meters.html')

#Страница нефти
def oil(request):
    if request.method == 'POST':
        oil = Oil.objects.filter(flag=True, date=request.POST.get('search'))
        return render(request, 'main/oil.html', {'oil': oil})
    else:
        oil = Oil.objects.filter(flag=True)
        return render(request, 'main/oil.html', {'oil': oil})

#Удаление записи из тыблицы oil (Запись не удаляется, а просто устанавливается flag=False)
def delete_oil(request, id):
    try:
        oil = Oil.objects.get(id=id)
        oil.flag = False
        oil.save()
        return HttpResponseRedirect('/oil')
    except Oil.DoesNotExist:
        return HttpResponseNotFound('<h2>Данных с таким id не существует!</h2>')

#Редактирование записи по id с таблицы oil
def edit_oil(request, id):
    try:
        oil = Oil.objects.get(id=id)

        if request.method == 'POST':
            oil.date = request.POST.get('date')
            oil.value = request.POST.get('value')
            oil.save()
            return HttpResponseRedirect('/oil')
        else:
            return render(request, 'main/edit_oil.html', {'oil': oil})
    except Oil.DoesNotExist:
        return HttpResponseNotFound('<h2>Запись в таблице отсутствует!</h2>')

#Создание записи в таблице oil
def create_oil(request):
    if request.method == 'POST':
        oil = Oil()
        oil.date = request.POST.get('date')
        oil.value = request.POST.get('value')
        oil.flag = True
        oil.save()
        return HttpResponseRedirect('/oil')
    else:
        return render(request, 'main/add_oil.html')