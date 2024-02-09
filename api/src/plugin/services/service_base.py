from abc import ABC,abstractmethod
from api.src.plugin.models.graph import Graph

class ServiceBase(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

class GraphLoadBase(ServiceBase):

    @abstractmethod
    def load_graph(self, configuration_params:dict) -> Graph:
        pass

    @abstractmethod
    def get_configuration_params(self) -> list:
        pass

class GraphDisplayBase(ServiceBase):

    @abstractmethod
    def show_graph(self,graph):
        pass