from django.shortcuts import render
from django.views.generic import ListView, DetailView

from applications.models import Application


class ApplicationList(ListView):
    model = Application


class ApplicationDetail(DetailView):
    model = Application
