from django.shortcuts import render, redirect
from AuthenticationApp.models import *
from django.contrib.auth.decorators import login_required

@login_required
def prd_view(request):
    
    data = ProductModel.objects.all()
    
    return render(request, 'product.html', {'data':data})

@login_required
def add_prd_view(request):
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        ProductModel.objects.create(
            product_name = product_name,
            category = category,
            description = description,
            price = int(price),
            quantity = int(quantity),
        )
        return redirect('prd')
    
    return render(request, 'add-prd.html')

@login_required
def edit_prd_view(request, eid):
    
    data = ProductModel.objects.get(id = eid)
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
    
        data.product_name = product_name
        data.category = category
        data.description = description
        data.price = int(price)
        data.quantity = int(quantity)
        
        data.save()

        return redirect('prd')
    
    return render(request, 'edit-prd.html',  {'data':data})

@login_required
def delete_prd_view(request, eid):
    
    ProductModel.objects.get(id = eid).delete()
    
    return redirect('prd')