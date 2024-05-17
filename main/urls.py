from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("databaseview", views.databaseView, name="databaseview"),
    path("creation", views.creation, name="creation"),
    path("editdatabase", views.editdatabase, name="editdatabase"),
    path("databaseView", views.databaseView, name="databaseView"),
    path("importdata", views.importdata, name="importdata")
]
