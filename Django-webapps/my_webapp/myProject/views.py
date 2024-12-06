from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import EmployeeModel

def index(request):
    return HttpResponse("Hello Folks!!!")
# Create your views here.

#create employee
def create_view(request):

    context={}
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'create_view.html', context)

#list employees
def list_view(request):
    context={}
    # context['dataset'] = EmployeeModel.objects.raw('SELECT * FROM EmployeeModel')
    context['dataset'] = EmployeeModel.objects.all()

    return render(request, 'list_view.html', context)

def detail_view(request,id):
    context={}
    context['data'] = EmployeeModel.objects.get(id=id)
    return render(request,'detail_view.html', context)

def update_view(request, id):
    context={}
    obj = get_object_or_404(EmployeeModel, id=id)
    form = EmployeeForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/detail/"+id)
    context["form"] = form

    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(EmployeeModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request, "delete_view.html", context)


