from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView): # using django template view generic class based view which means we only need to specify template name to use
    template_name = 'home.html'
