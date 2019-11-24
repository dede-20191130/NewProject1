import random
from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse


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


# d = {
#     'is_visible': True,
#     'empty_str': 'イヴェルカーナFROST',
# }
# return render(request, 'if.html', d)


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
