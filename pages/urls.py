"""
pages/urls.py
"""
######################## Function based view #################33
# from django.urls import path
# from .views import homePageView
#
# urlpatterns = [
#     path('', homePageView, name='home'),
# ]

from django.urls import path
from .views import HopePageView, AboutPageView

urlpatterns = [
    path('', HopePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

]