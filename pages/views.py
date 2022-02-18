from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
# def homePageView(request):
#     return HttpResponse('Hello, World')
#
######################################################

from django.views.generic import TemplateView

class HopePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
