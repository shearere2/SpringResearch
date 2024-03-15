from django.urls import path
from elevation import views

urlpatterns = [
    path("", views.home, name="home"),
]