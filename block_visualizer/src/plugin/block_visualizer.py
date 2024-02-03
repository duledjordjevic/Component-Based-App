from api.src.plugin.models.graph import Graph
from api.src.plugin.services.service_base import GraphDisplayBase
from django.template.loader import render_to_string
from jinja2 import Environment, FileSystemLoader



class GraphBlockVisualizer(GraphDisplayBase):
    def identifier(self):
        return "GraphBlockVisualizer"
    
    def name(self):
        return "Display graph in block format"
    
    def show_graph(self, graph: Graph):
        context = {"graph" : graph}
        template_dir = "../block_visualizer/src/plugin"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("mainView.html")
        return template.render(context)
    