from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Message
from .forms import MessageForm


def index(request, is_delete=False):
    index_date = {
        'messages': Message.objects.all(),
        'is_delete': is_delete
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


@require_POST
def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('crud:index_after_delete', is_delete=True)
