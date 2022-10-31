from django.urls import path
from .import views 
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
    path('login/',views.LoginApi.as_view()),
    path('sendmoney/',views.sendmoney),
    path('sendmoney/<int:pk>/', views.sendoneyDetail),
    path('registration/',views.Regist),
    path('loan/', views.LoanApi.as_view()),
    path('loan/<int:pk>/', views.LoanApiDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)