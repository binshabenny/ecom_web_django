from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def pdt_description(request):
    return render(request,'pdt_description.html')

def single_product(request):
    return render(request,'single_product.html')
   

