from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from main.models import *

# Create your views here.
def index(request):
    return render(request, 'metric/metric_index.html')

def value(request):
    value = MeterValue.objects.filter(flag=True)
    return render(request, 'metric/metric_value.html', {'value': value})

def value_add(request):
    if request.method == 'POST':
        meter_value = MeterValue()
        meter_value.meter_id = request.POST.get('id_meter')
        meter_value.value_first = request.POST.get('start')
        meter_value.value_last = request.POST.get('end')
        if request.POST.get('fact') == '':
            meter_value.value_fact = float(request.POST.get('end')) - float(request.POST.get('start'))
        else:
            meter_value.value_fact = request.POST.get('fact')
        meter_value.date_add = request.POST.get('date')
        meter_value.palse_id = request.POST.get('plase')
        meter_value.flag = True
        meter_value.save()
        return HttpResponseRedirect('/metric/value/')
    else:
        meters = Meters.objects.all()
        plase = Plase.objects.all()
        return render(request, 'metric/value_add.html', {"meters": meters, "plase": plase})

def delete_value(request, id):
    try:
        meter_value = MeterValue.objects.get(id=id)
        meter_value.flag = False
        meter_value.save()
        return HttpResponseRedirect('/metric/value/')
    except MeterValue.DoesNotExist:
        return HttpResponseNotFound('<h1>При удалении что-то пошло не так😞</h1>')

def edit_value(request, id):
    meters = Meters.objects.all()
    plase =Plase.objects.all()
    return render(request, 'metric/value_edit.html', {"meters": meters, "plase": plase})