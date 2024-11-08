from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("tasks/", views.task_list_create, name="task-list-create"),
    path("tasks/<int:pk>/", views.task_update_delete, name="task-update-delete"),  
]
