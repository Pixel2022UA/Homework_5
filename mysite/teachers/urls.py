from django.urls import path

from . import views

urlpatterns = [
    path("", views.generate_teachers, name="generate-teachers"),
]
