from django.http import HttpResponse
from django.shortcuts import render

from find_data import GetDataForPlot
import json


def home(request):
    g = GetDataForPlot()
    companyData = {
        "months": g.get_months(),
        "headcounts": g.get_data()
    }

    context = {
        'companyData': json.dumps(companyData),
    }
    return render(request, 'index.html', context)
