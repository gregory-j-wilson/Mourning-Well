from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("prompts/", views.prompt_list, name="prompt_list"),
    path("prompts/<int:pk>/", views.prompt_detail, name="prompt_detail"),
    path("resources/", views.resource_list, name="resource_list"),
    path("journal/", views.journal, name="journal"),
]
