from django.urls import path

from . import views

app_name = "todos"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add", views.add, name="add"),
    path("<int:pk>/", views.DetailView.as_view(), name="todo"),
    path("<int:todo_id>/update/", views.update, name="update"),
    path("<int:todo_id>/edit/", views.edit, name="edit"),
    path("<int:todo_id>/replicate/", views.replicate, name="replicate"),
    path("<int:todo_id>/delete/", views.delete, name="delete"),
]
