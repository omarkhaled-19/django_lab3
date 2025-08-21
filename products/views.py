from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from products.models import techProducts
from categories.models import techCategories
# Create your views here.
def productspage(request):
    return render(request,'index.html')

def landingpage(request):
    return render(request,'landing.html')

def test_layout(request):
    return render(request,'layouts/base.html')

def all_products(request):
    products = techProducts.objects.all()
    return render(request,'all.html',context={'products':products})

def show_product(request,product_id):
    product = get_object_or_404(techProducts,id=product_id)
    return render(request,'show.html',context={'product':product})

def delete_product(request,product_id):
    product = get_object_or_404(techProducts,id=product_id)
    product.delete()
    return redirect('../all')

def create_product(request):
    categories = techCategories.objects.all()

    print(request)
    if request.method == 'POST':
        pname = request.POST.get('name')
        pprice = request.POST.get('price')
        pinstock = request.POST.get('instock')
        pdescription = request.POST.get('description')
        pimage = request.FILES.get('image')
        pcategory_id = request.POST.get('category')

        product = techProducts()
        product.name = pname
        product.price = pprice
        product.instock = pinstock
        product.description = pdescription
        product.image = pimage
        product.category_id = pcategory_id  
        product.save()
        return redirect('/products/all')
    
    return render(request,'create.html', context={'categories':categories})


