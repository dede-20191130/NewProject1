import random
from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import HttpResponse

from . import models


def hello_world(request):
    return HttpResponse('Hello World!')


def hello_template(request):
    d = {
        'hour': datetime.now().hour,
        'minite': datetime.now().minute,
        'message': '指定文字列表示：Python練習中',
    }
    return render(request, 'index.html', d)


def hello_if(request):
    randomBool = random.random() * 2 > 1

    d = {
        'is_visible': randomBool,
        'empty_str': 'イヴェルカーナFROST',
    }
    return render(request, 'if.html', d)


def hello_for(request):
    d = {
        'objects': range(10),
    }
    return render(request, 'for.html', d)


def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)


from . import forms


def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms.html', d)


def hello_forms2(request):
    d = {
        'form': forms.SampleForm(),
    }
    return render(request, 'form_samples.html', d)


def hello_models(request):
    form = forms.HelloForm(request.POST or None)
    if form.is_valid():
        models.Hello.objects.create(**form.cleaned_data)
        return redirect('hello:hello_models')

    d = {
        'form': form,
        'hello_qs': models.Hello.objects.all().order_by('-id')
    }
    return render(request, 'models.html', d)