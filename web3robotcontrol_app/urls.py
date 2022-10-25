from django.urls import path
from .views import addblockView, showblockView, stillExists

urlpatterns = [
    path('addblock/', addblockView, name='addblock'),
    path('showblock/', showblockView, name='showblock'),
    path('showblock/exist/', stillExists, name='exist'),
]