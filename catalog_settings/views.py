from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm

def category_details(request, url):
	cart_product_form= CartAddProductForm()
	product = get_object_or_404(Category, url=url)
	category = Category.objects.filter(url=url)
	categories = Category.objects.all()
	prd=products.objects.filter(catid=category[0])
	data={'prd':prd,'cart_product_form':cart_product_form,'categories':categories}
	return render(request,"shopping.html",data)


def shopping(request):
    prd=products.objects.all()
    categories = Category.objects.all()
    
    cart_product_form= CartAddProductForm()
    #data={'prd':prd,'cart_product_form':cart_product_form}
    data={'prd':prd,'cart_product_form':cart_product_form,'categories':categories}

    return render(request,"shopping.html",data)



