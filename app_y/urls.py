from django.urls import path
from .views import *

urlpatterns = [
    path('y/',y_index,name='yp')
]