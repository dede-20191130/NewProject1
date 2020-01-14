from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Message
from .forms import MessageForm


def index(request):
    index_date = {
        'messages': Message.objects.all(),
    }
    return render(request, 'crud/index.html', index_date)


def add(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('crud:index')

    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html', d)


def edit(request, editing_id):
    message = get_object_or_404(Message, id=editing_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.message = form.cleaned_data['message']
            message.type = form.cleaned_data['type']
            message.save()
            return redirect('crud:index')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        form = MessageForm({
            'message': message.message,
            'type': message.type
        })
    d = {
        'form': form,
    }

    return render(request, 'crud/edit.html', d)


def delete(request):
    return HttpResponse('Delete')
