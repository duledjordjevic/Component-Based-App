import pkg_resources
from django.apps import AppConfig

def load_plugins(group):
        plugins = []
        for ep in pkg_resources.iter_entry_points(group=group):
            p = ep.load()
            print("{} {}".format(ep.name, p))
            plugin = p()
            plugins.append(plugin)
        return plugins

class Loader():

    def __init__(self):
        self.data_sources = []
        self.visualizers = []    
    
    def load_data_sources(self):
        self.data_sources = load_plugins('graph.load')

    def load_visualizers(self):
        self.visualizers = load_plugins('graph.visualizer')

    @property
    def data_sources(self): 
         return self.data_sources 
    
    @property
    def visualizers(self): 
         return self.visualizers