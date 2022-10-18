from django.urls import path
from .import views 
from .views import *

urlpatterns = [
    path('sendmoney/',views.sendmoney),
    path('sendmoney/<int:pk>/', views.sendoneyDetail),
    path('registration/',views.Regist)
]
