from django.shortcuts import render, Http404

# Create your views here.
from .models import Product


def search(request):
  try:
    q= request.GET.get("q")
  except: q=None
  if q:
    products = Product.objects.filter(title__icontains=q)
    template = 'products/results.html'
    context = {"query" : q , "products":products}
  else:
    context = {}
    template = 'products/home.html'
  return render(request , template, context)


def home(request):
  products = Product.objects.all()
  context = {"products" : products}
  template = 'products/home.html'
  return render(request , template, context)


def all(request):
  products = Product.objects.all()
  context = {"products" : products}
  template = 'products/all.html'
  return render(request , template, context)


def single(request, slug):
  try:
    product = Product.objects.get(slug=slug)
    context = {"product" : product}
    template = 'products/single.html'
    return render(request , template, context)
  except :
    raise Http404
