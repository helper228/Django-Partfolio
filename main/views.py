from django.shortcuts import render
from django.shortcuts import redirect
import logging
import requests
from .models import *
# Create your views here.


def Main(request):
    if request.method == 'POST':
        name = request.POST.get('c_name')
        mail = request.POST.get('c_email')
        message = request.POST.get('c_message')
        url = f"https://api.telegram.org/bot1710847434:AAER0ThTJ2FbzkTYisIca0QEeJ9DXl_hyoU/sendMessage?chat_id=-574336421&text=Имя: {name} \nemail:{mail} \nсообщение: {message}"
        requests.post(url)

        Massege.objects.create(Name=name, gmail=mail, massege=message)

        return redirect('/answer')

    return render(request, 'index.html',{'ok':''})

def answer(request):
    return render(request, 'answer.html')
