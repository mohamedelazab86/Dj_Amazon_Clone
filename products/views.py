from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product

# Create your views here.

# create crud opertion by classed based view

class ProductList(ListView):
    model=Product


class ProductDetail(DetailView):
    model=Product