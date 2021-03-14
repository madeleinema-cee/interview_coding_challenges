import json

from django.http import HttpResponse
from django.shortcuts import render

from retrieve_company_data import RetrieveCompanyData


def home(request):
    r = RetrieveCompanyData()
    months, headcounts = r.main()

    companyData = {
        "months": months,
        "headcounts": headcounts
    }

    context = {
        'companyData': json.dumps(companyData),
    }

    return render(request, 'index.html', context)
