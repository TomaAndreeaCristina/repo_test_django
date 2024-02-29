from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel


# Create your views here.

class ServiciiDetailsView(DetailView):
    template_name = "servicii/detalii.html"
    model = ServiciiModel #select all from serviciimodelwhere id=pk

class ServiciiListView(ListView):
    template_name = "servicii/all.html"
    model = ServiciiModel  # select all from serviciimodelwhere id=pk

class ServiciiUpdateView(UpdateView):
    form_class = ServiciiForm
    template_name = "create_update_form.html"
    model = ServiciiModel
    success_url = reverse_lazy('servicii-all')

class ServiciiDeleteView(DeleteView):
    template_name = "delete.html"
    model = ServiciiModel
    success_message = "Service deleted with success"
    success_url = reverse_lazy('serviciu-all')

class ServiciiCreateView(CreateView):
    form_class = ServiciiForm
    template_name = "create_update_form.html"
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')