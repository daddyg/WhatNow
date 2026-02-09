from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sport/<slug:sport_name>/", views.sportDetail, name="detail"),
]