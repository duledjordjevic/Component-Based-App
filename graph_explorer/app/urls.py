from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("mainView", views.show_main_view, name="mainView"),
    path('get_nodes/<int:id>/', views.get_nodes, name='get_nodes'),
    path("filter", views.filter, name="filter"),
    path("get_configuration_params", views.get_configuration_params, name="get_configuration_params"),
    path("add_workspace", views.add_workspace, name="add_workspace"),
    path("workspace/<int:index>/", views.get_workspace, name="workspace")
]