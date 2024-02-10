from django.shortcuts import render, redirect
from django.http import JsonResponse
from core.src.use_cases.main import Core

# core = Core()
workspaces = [Core()]
currentWorkspace = 0

def index(request):
    context = {
        "data_sources": workspaces[currentWorkspace].loader.data_sources.keys,
        "visualizers": workspaces[currentWorkspace].loader.visualizers.keys,
        "workspaceLength": range(len(workspaces))
    }

    return render(request, 'index.html',context)

def add_workspace(request):
    if request.method == 'POST':
        workspaces.append(Core())
    print(len(workspaces))

def get_workspace(request, index):
    if request.method == 'GET':
        global currentWorkspace
        currentWorkspace = index
        print(workspaces)
        print("Index:", index)
        
        context = {"data_sources":workspaces[currentWorkspace].loader.data_sources.keys,
                    "visualizers": workspaces[currentWorkspace].loader.visualizers.keys,
                    "workspaceLength": range(len(workspaces))}
        mainView = workspaces[index].load_workspace()
        if mainView:
            context["mainView"] = mainView
        return render(request, 'index.html',context)
    
def show_main_view(request):
    if request.method == 'POST':
        visualizerPlugin = request.POST.get("visualizer",False)
        sourcePlugin = request.POST.get("source", False)

        configurationParams = {}
        for key, value in request.POST.items():
            if key != "source" and key != "visualizer":
                configurationParams[key] = value

            if value == "":
                return render(request, 'index.html',{"popupFormInvalid":True,"data_sources":workspaces[currentWorkspace].loader.data_sources.keys,
                                                "visualizers": workspaces[currentWorkspace].loader.visualizers.keys,
                                                "workspaceLength": range(len(workspaces))})
    
    print(currentWorkspace)
    return render(request, 'index.html',{'mainView':workspaces[currentWorkspace].load_main_view(sourcePlugin, visualizerPlugin, configurationParams),
                                         "data_sources":workspaces[currentWorkspace].loader.data_sources.keys,
                                        "visualizers": workspaces[currentWorkspace].loader.visualizers.keys,
                                        "workspaceLength": range(len(workspaces))})


def get_nodes(request, id):
    if request.method == 'GET':
        if id == 0:
            return JsonResponse(workspaces[currentWorkspace].graph.find_node_which_have_children())
        return JsonResponse(workspaces[currentWorkspace].graph.find_children(id))
    return JsonResponse({})


def filter(request):
    if request.method == 'POST':
        searchText = request.POST.get("search_text",False)
        key = request.POST.get("key", False)
        comparison_operator = request.POST.get("comparison_operator", False)
        value = request.POST.get("value", False)

        result, isValid = workspaces[currentWorkspace].filter_graph(searchText, key, value, comparison_operator)

        context = {
            'mainView': result,
            "data_sources": workspaces[currentWorkspace].loader.data_sources.keys,
            "visualizers": workspaces[currentWorkspace].loader.visualizers.keys,
            "workspaceLength": range(len(workspaces))
        }

        if not isValid:
            context["filterFormInvalid"] = True

        return render(request, 'index.html', context)


def get_configuration_params(request):

    if request.method == 'GET':
        visualizerPlugin = request.GET.get("visualizer", False)
        sourcePlugin = request.GET.get("source", False)

        results = workspaces[currentWorkspace].get_configuration_params(sourcePlugin)

        return JsonResponse({"configuration_params": results})
