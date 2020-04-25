from django.shortcuts import render, HttpResponse
import requests
from .metrics import get_metrics


def api(request):
    # https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01

    api_url = 'https://api.exchangeratesapi.io/history'
    params = dict(request.GET)

    response = requests.get(api_url, params=params)
    data = response.json()
    metrics = get_metrics(data)

    return HttpResponse(str(metrics))
