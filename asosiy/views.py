from django.shortcuts import render
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        content = {
            'bolimlar':Bolim.objects.all()[:7]
        }
        return render(request, 'page-index.html', content)

class HomeLoginsiz(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class MahsulotlarView(View):
    def get(self, request, pk):
        content = {
            'mahsulotlar': Mahsulot.objects.filter(bolim__id=pk),

        }
        return render(request, 'page-listing-grid.html', content)

class BolimView(View):
    def get(self, request):
        content = {
            'bolim': Bolim.objects.all(),
        }
        return render(request, 'page-category.html', content)


# Create your views here.
