from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.urls import reverse

from . import models
from . import forms

# Create your views here.


def index(request):
    num = models.LinkModel.objects.aggregate(Count('lid'))['lid__count']
    context = {
        'num': num,
        'links': models.LinkModel.objects.order_by('-count')
    }
    return render(request, 'linker/index.html', context)


'''
def redirect_test(request):
    return render(request, 'linker/redirect.html')
'''


def redirect_url(request, lid):
    try:
        link = models.LinkModel.objects.get(lid=lid)
        link.count += 1
        link.save()
    except models.LinkModel.DoesNotExist:
        return HttpResponse(f'Link not found!')
    return render(request, 'linker/redirect.html', {'link': link})


def new_link(request):
    if request.method != 'POST':
        form = forms.LinkForm()
    else:
        form = forms.LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('linker:index'))

    context = {'form': form}
    return render(request, 'linker/new_link.html', context)
