from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.blank, name = "blank"),
    path("index/", views.index, name = "index"),
    path("update/<int:current_id>", views.update, name = "update"),
    path("delete/<int:current_id>", views.delete, name = "delete"),
    path("create/", views.create, name = "create"),
    path("signin/", views.signin, name = "signin"),
    path("signup/", views.signup, name = "signup"),
    path("signout/", views.signout, name = "signout"),
]