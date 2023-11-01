# Create your views here.
import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from todos.models import Todo


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todolist'

    def get_queryset(self):
        return Todo.objects.order_by('status', '-priority', '-createdat')


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/todo.html'


def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    priority = request.POST.get('priority')
    Todo.objects.create(name=name, description=description, priority=priority)
    return HttpResponseRedirect(reverse("todos:index"))


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse("todos:index"))


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.status = True
    todo.updatedat = datetime.datetime.now()
    todo.save()
    return HttpResponseRedirect(reverse("todos:index"))


def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    name = request.POST.get('name')
    description = request.POST.get('description')
    priority = request.POST.get('priority')
    todo.updatedat = datetime.datetime.now()
    todo.name = name
    todo.description = description
    todo.priority = priority
    todo.save()
    return HttpResponseRedirect(reverse("todos:index"))


def replicate(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.status = True
    todo.updatedat = datetime.datetime.now()
    todo.save()
    return HttpResponseRedirect(reverse("todos:index"))
