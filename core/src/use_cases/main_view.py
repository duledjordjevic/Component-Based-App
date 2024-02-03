from django.apps.registry import apps
from django.shortcuts import render
from api.src.plugin.models.graph import Graph
from core.src.use_cases.load import Loader


class MainView():

    def load_main_view(self,data_source_key:str, visualizer_key:str,loader: Loader):
        data_source = loader.data_sources[data_source_key]
        retVal = loader.visualizers[visualizer_key].show_graph(data_source.load_graph())
        return retVal

