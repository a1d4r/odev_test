from django.shortcuts import render, HttpResponse
import requests
from .metrics import get_metrics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings


@api_view(['GET'])
def api(request):
    # query parameters
    params = dict(request.GET)
    # response from external api
    response = requests.get(settings.EXCHANGE_API_URL, params=params)
    # data from external api
    data = response.json()
    # calculated metrics
    metrics = get_metrics(data)
    return Response(metrics)
