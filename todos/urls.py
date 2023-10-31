from django.urls import path

from . import views

app_name = "todos"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add", views.add, name="add"),
    path("<int:pk>/", views.DetailView.as_view(), name="todo"),
    path("<int:id>/update/", views.update, name="update"),
    path("<int:id>/delete/", views.delete, name="delete"),
]
