from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view()),
    path('<int:pk>/mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulot/<int:pk>/', DetalView.as_view()),
]