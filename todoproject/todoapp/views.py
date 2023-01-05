from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import TodoForm
from .models import Task


# Create your views here.
def addtask(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', )
        priority = request.POST.get('priority', )
        date = request.POST.get('date', )
        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'task1': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})


def __str__(self):
    return self.name


# class based functions

class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task1'

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')


class updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task1'

    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})
