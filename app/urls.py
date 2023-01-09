from django.urls import path
from app import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("Post/",views.Post,name="Post"),
    path("Read/",views.Read,name="Read"),
    path("update/<int:id>",views.Update,name="update"),
    path("delete/<int:id>",views.Delete,name="delete"),
]

