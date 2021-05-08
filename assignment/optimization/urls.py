from django.urls import path
from . import views

app_name = "optimize"

urlpatterns = [
    path("", views.index, name="index")
]