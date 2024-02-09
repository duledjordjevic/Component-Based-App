from django.shortcuts import render, redirect
from django.http import JsonResponse
from core.src.use_cases.main import Core

core = Core()


def index(request):
    context = {
        "data_sources": core.loader.data_sources.keys,
        "visualizers": core.loader.visualizers.keys
    }

    return render(request, 'index.html',context)

def show_main_view(request):
    if request.method == 'POST':
        visualizerPlugin = request.POST.get("visualizer",False)
        sourcePlugin = request.POST.get("source", False)

    if not(visualizerPlugin and sourcePlugin):
        return render(request, 'index.html',{"formInvalid":True,"data_sources":core.loader.data_sources.keys,
                                        "visualizers": core.loader.visualizers.keys})
    
    return render(request, 'index.html',{'mainView':core.load_main_view(sourcePlugin,visualizerPlugin),
                                         "data_sources":core.loader.data_sources.keys,
                                        "visualizers": core.loader.visualizers.keys})


def get_nodes(request, id):
    if request.method == 'GET':
        if id == 0:
            return JsonResponse(core.graph.find_node_which_have_children())
        return JsonResponse(core.graph.find_children(id))
    return JsonResponse({})


def filter(request):
    if request.method == 'POST':
        searchText = request.POST.get("search_text",False)
        key = request.POST.get("key", False)
        comparison_operator = request.POST.get("comparison_operator", False)
        value = request.POST.get("value", False)

        result, isValid = core.filter_graph(searchText, key, value, comparison_operator)

        context = {
            'mainView': result,
            "data_sources": core.loader.data_sources.keys,
            "visualizers": core.loader.visualizers.keys
        }

        if not isValid:
            context["filterFormInvalid"] = True

        return render(request, 'index.html', context)
