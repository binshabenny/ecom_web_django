from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name='index_page'),
    path('products/', views.products,name='products_page'),
    path('pdt_description/', views.pdt_description, name='description'),
    path('single_product/', views.single, name='single'),
    path('contact/', views.contacts,name='contacts'),



]
