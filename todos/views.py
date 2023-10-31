# Create your views here.

from django.views import generic

from todos.models import Todo


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todolist'

    def get_queryset(self):
        return Todo.objects.order_by('-createdat')


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/todo.html'


def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    priority = request.POST.get('priority')
    print(name, description, priority)


def delete(request, todo_id):
    print(todo_id)


def update(request, todo_id):
    print(todo_id)
