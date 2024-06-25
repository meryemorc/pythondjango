from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from datetime import date
from .models import Product, Brand
from django.http import HttpResponse, HttpResponseNotFound

data = {
    "Apple": "Apple markasına ait ürünler",
    "Samsung": "Samsung markasına ait ürünler",
    "Huawei": "Huawei markasına ait ürünler",
    "Xiaomi": "Xiaomi markasına ait ürünler",
}

def index(request):
    urunler = Product.objects.all()
    markalar = Brand.objects.all()
       
    return render(request, 'product/index.html', {
        'brand': markalar,
        'products': urunler
    })

def details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/details.html', context)

def getProductByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'product/product.html', {
            'category': category_name,
            'category_text': category_text
        })
    except KeyError:
        return HttpResponseNotFound("<h1>Yanlış kategori seçimi</h1>")

def getProductByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("Yanlış kategori seçimi")

    category_name = category_list[category_id - 1]
    redirect_url = reverse('get_product_by_category', args=[category_name])

    return redirect(redirect_url)
