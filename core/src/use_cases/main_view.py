from django.apps.registry import apps
from django.shortcuts import render
from api.src.plugin.models.graph import Graph


def force_layout(request):
    plugins = apps.get_app_config('block_visualizer').plugins
    graph: Graph = plugins[0].load_graph()
    return render(request,"mainView.html",
                  {"title":"Force layout graph",
                   "plugins": plugins,
                   "graph" : graph})