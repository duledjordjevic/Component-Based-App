from django.urls import path

from . import views 

urlpatterns = [
    path("", views.base, name="base"),
    path("mainView", views.show_main_view, name="mainView")
]