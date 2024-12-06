from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect)
from django.http import HttpResponse
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def task_view(request):
    context={}
    form = TaskForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/tasks/')

    context['dataset'] = TaskModel.objects.all()
    return render(request, 'task_template.html', context)

def update_view(request, id):
    context={}
    obj = get_object_or_404(TaskModel, id=id)
    form = TaskForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/tasks/')
    context["form"] = form

    return render(request, "task_template.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(TaskModel, id=id)
    print("obj found: ", obj)
    # if request.method == 'POST':
    obj.delete()
    print('obj deleted')
    return redirect('/tasks/')
    print('after redirect')
    return render(request, "task_template.html", context)
