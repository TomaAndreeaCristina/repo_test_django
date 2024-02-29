from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from servicii.models import ServiciiModel


# Create your views here.
def home(request):
    return render(request, template_name='home/home.html', context={})


class HomeView(ListView):  # alternativa pentru creare unui view dinamic(listView), static(TemplateView)
    template_name = 'home/home.html'
    model= ServiciiModel   #select all pentru ca mosteneste ListView
