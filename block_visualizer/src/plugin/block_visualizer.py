from api.src.plugin.models.graph import Graph
from api.src.plugin.services.service_base import GraphDisplayBase
from django.template.loader import render_to_string

class GraphBlockVisualizer(GraphDisplayBase):
    def identifier(self):
        return "GraphBlockVisualizer"
    
    def name(self):
        return "Display graph in block format"
    
    def show_graph(self, graph: Graph):
        context = {"graph" : graph}
        return render_to_string("mainView.html", context)