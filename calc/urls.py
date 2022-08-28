from ast import pattern
# from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.urls import path

from . import views
urlpatterns= [

path('',views.home, name='home')
]
