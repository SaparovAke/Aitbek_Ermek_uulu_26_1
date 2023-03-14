from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.

def hello_page_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! its my project')

def date_page_view(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(f'{current_time}')

def bye_page_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')

