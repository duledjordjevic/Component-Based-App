from api.src.plugin.models.graph import Graph
from api.src.plugin.services.service_base import GraphDisplayBase
from jinja2 import Environment, FileSystemLoader


class GraphSimpleVisualizer(GraphDisplayBase):
    def identifier(self):
        return "GraphSimpleVisualizer"

    def name(self):
        return "Display graph in simple format"

    def show_graph(self, graph: Graph):
        context = {"graph": graph}
        template_dir = "../simple_visualizer/src/plugin"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("mainView.html")
        return template.render(context)