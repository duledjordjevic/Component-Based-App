from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("mainView", views.show_main_view, name="mainView"),
    path('get_nodes/<int:id>/', views.get_nodes, name='get_nodes')
]