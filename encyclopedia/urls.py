from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path("vishvakosh/create", views.create_entry, name="createEntry"),
    path("vishvakosh/random", views.random_entry, name="randomEntry"),
    path("wikvishvakoshi/search", views.search_entry, name="searchEntry"),
    path("vishvakosh/<str:entry>", views.view_entry, name="viewEntry"),
    path("wikvishvakoshi/<str:entry>/edit", views.edit_entry, name="editEntry"),
]