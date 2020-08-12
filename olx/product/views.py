from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count


# Create your views here.

def productlist(request, category_slug=None):
    category = None

    productlist = Product.objects.all()

    categoryList = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        productlist = productlist.filter(category=category)

    paginator = Paginator(productlist, 1)

    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    template = 'Product/product_list.html'

    context = {'product_list': productlist, 'category_list': categoryList, 'category': category}

    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_detail': productdetail, 'product_images': productimages}
    return render(request, template, context)
