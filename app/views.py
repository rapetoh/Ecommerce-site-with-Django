from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Products



# Create your views here.
def indexx(request):
    return render(request,'app/base.html')

def home(request):
    return render(request, 'app/home.html')

class CategoryView(View):
    def get(self,request,val):
        prdct=Products.objects.filter(category=val)
        title=Products.objects.filter(category=val).values('title')
        return render(request,'app/category.html',locals())

class ProductDetail(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        return render(request,'app\product_detail.html',locals())