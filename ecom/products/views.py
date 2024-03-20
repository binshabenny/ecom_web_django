from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    product_list = Product.objects.all()
    product_paginator = Paginator(product_list,6)
    product_list= product_paginator.get_page(1)
    context  = {'products':product_list}
    return render(request,'products.html',context)

def pdt_description(request):
    product_list = Product.objects.all()
    context  = {'products':product_list}
    return render(request,'pdt_description.html',context)

def single(request):
    return render(request,'single.html')

def contacts(request):
    return render(request,'contacts.html') 
   

