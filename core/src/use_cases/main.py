from core.src.use_cases.load import Loader
from api.src.plugin.models.graph import Graph


class Core:

    def __init__(self):
        self.graph: Graph = None
        self.loader: Loader = Loader()
        self.loader.load_data_sources()
        self.loader.load_visualizers()
        
    
    def load_main_view(self,  data_source_key:str, visualizer_key:str):
        data_source = self.loader.data_sources[data_source_key]
        self.graph = data_source.load_graph()
        retVal = self.loader.visualizers[visualizer_key].show_graph(self.graph)
        return retVal