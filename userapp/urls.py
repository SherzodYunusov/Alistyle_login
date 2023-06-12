from django.urls import path
from .views import *


urlpatterns = [
    path('qoshish/', QoshishView.as_view()),
    path('register/', RegisterView.as_view())
]