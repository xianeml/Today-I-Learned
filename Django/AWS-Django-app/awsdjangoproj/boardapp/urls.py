from django.urls import path
from boardapp.views import *

urlpatterns = [
    path('', main_page, name='main'),
]