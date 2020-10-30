import os
from django.http import HttpResponse


def index(request):
    os.system('python main.py')
    return HttpResponse('<h1>test</h1>')
