import pkg_resources
from django.apps import AppConfig

def load_plugins(group) -> dict:
        plugins = {}
        
        for ep in pkg_resources.iter_entry_points(group=group):
            p = ep.load()
            print("{} {}".format(ep.name, p))
            plugin = p()
            plugins[plugin.identifier()] = plugin
        return plugins

class Loader():

    def __init__(self):
        self.data_sources = {}
        self.visualizers = {}
    
    def load_data_sources(self):
        self.data_sources = load_plugins('graph.load')

    def load_visualizers(self):
        self.visualizers = load_plugins('graph.visualizer')

    @property
    def data_sources(self): 
        return self._data_sources 
    
    @data_sources.setter
    def data_sources(self, value):
        self._data_sources = value
    
    @property
    def visualizers(self): 
        return self._visualizers
    
    @visualizers.setter
    def visualizers(self, value):
        self._visualizers = value