from django.shortcuts import render
from . import runner


def index(request):
    runner.Telegram(wait=False)
    return render(request, 'index.html')
