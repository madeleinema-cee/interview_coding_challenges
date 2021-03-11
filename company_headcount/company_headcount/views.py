from django.http import HttpResponse
from django.shortcuts import render

from find_data import GetDataForPlot


def home(request):
    g = GetDataForPlot()
    months = g.get_months()
    print(months)
    context = {
        'months': months
    }
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse('<h1>About</h1>')
