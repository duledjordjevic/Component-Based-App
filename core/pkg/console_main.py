import pkg_resources
from api.src.plugin.services.service_base import GraphLoadBase
from typing import List



def console_menu(*args, **kwargs):
    plugins: List[GraphLoadBase] = kwargs.get("graph_load", [])

    if not plugins:
        print("Nije prepoznati nijedan plugin!")
        return
    greska = False
    poruka = None
    while True:
        print("-----------------------------------")
        if greska:
            print("Uneli ste pogresnu vrednost za opciju")
            greska = False
        if poruka:
            print(poruka)
        print("Izaberite broj opcije:")
        for i, plugin in enumerate(plugins):
            print(f"{i} {plugin.identifier()} {plugin.name()}")
        print(f"{len(plugins)} za izlaz")
        try:
            izbor = int(input("Unesite redni broj opcije:"))
        except:
            greska = True
            continue
        if izbor == len(plugins):
            return
        elif 0 <= izbor < len(plugins):
            poruka = izabrana_opcija(plugins[izbor], **kwargs)
        else:
            greska = True


def izabrana_opcija(plugin: GraphLoadBase, **kwargs):
    try:
        if isinstance(plugin, GraphLoadBase):
            graph = kwargs["graph"]
            pomocna_lista = plugin.load_graph()
            del graph[:]
            
            for node in pomocna_lista.nodes:
                print(node)
            for edge in pomocna_lista.edges:
                print(edge)

            return "Ucitani fakulteti"
    except Exception as e:
        print(f"Error: {e}")

def load_plugins(group):

    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()

        print(f"{ep.name} {p}")
        
        plugin = p()
        plugins.append(plugin)
    return plugins




def main():
    try:
        graph_load = load_plugins("graph.load")

    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        graph = []
        console_menu(graph_load=graph_load,
                     graph=graph)

    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()