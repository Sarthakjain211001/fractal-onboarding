from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from django.http import HttpResponse
from .forms import ProductForm
from .models import ProductModel

#create product
def create_view(request):
    context={}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'create_view.html', context)

#list products
def list_view(request):
    context={}
    context['dataset'] = ProductModel.objects.all()

    return render(request, 'product_list_view.html', context)

#detail of a product
def detail_view(request,id):
    context={}
    context['data'] = ProductModel.objects.get(id=id)
    return render(request,'product_detail_view.html', context)

#update a product
def update_view(request, id):
    context={}
    obj = get_object_or_404(ProductModel, id=id)
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/product/detail/"+id)
    context["form"] = form

    return render(request, "update_view.html", context)

#delete a product
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(ProductModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/product/list")
    return render(request, "delete_view.html", context)
