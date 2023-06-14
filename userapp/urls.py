from django.urls import path
from .views import *


urlpatterns = [
    path('qoshish/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view)
]