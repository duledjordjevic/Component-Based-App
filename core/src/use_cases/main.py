from core.src.use_cases.load import Loader
from api.src.plugin.models.graph import Graph


class Core:

    def __init__(self):
        self.graph: Graph = None
        self.loader: Loader = Loader()
        self.loader.load_data_sources()
        self.loader.load_visualizers()
        self.current_visualizer: str = ""
        
    
    def load_main_view(self,  data_source_key:str, visualizer_key:str):
        data_source = self.loader.data_sources[data_source_key]
        self.graph = data_source.load_graph()
        self.current_visualizer = visualizer_key
        retVal = self.loader.visualizers[visualizer_key].show_graph(self.graph)
        return retVal

    def filter_graph(self, searchText, key, value, comparison_operator):
        if self.graph is not None and len(self.graph.nodes) > 0:
            if key != "":
                retVal = self.loader.visualizers[self.current_visualizer].show_graph(self.graph)
                isValid = self.graph.filter(key, value, comparison_operator)

                if not isValid:
                    return retVal, False

            if searchText != "":
                self.graph.search(searchText)

        retVal = self.loader.visualizers[self.current_visualizer].show_graph(self.graph)
        return retVal, True
