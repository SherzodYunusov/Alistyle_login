from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                'bolimlar':Bolim.objects.all()[:7]
            }
            return render(request, 'page-index.html', content)
        return redirect('/')

class HomeLoginsiz(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class MahsulotlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            content = {
                'mahsulotlar': Mahsulot.objects.filter(bolim__id=pk),

            }
            return render(request, 'page-listing-grid.html', content)
        return redirect('/')
class BolimView(View):
    def get(self, request):
        content = {
            'bolim': Bolim.objects.all(),
        }
        return render(request, 'page-category.html', content)


class DetalView(View):
    def get(self, request, pk):
        content = {
            'mahsulot': Mahsulot.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html', content)

# Create your views here.
