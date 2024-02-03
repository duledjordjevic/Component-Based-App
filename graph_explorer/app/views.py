from django.shortcuts import render
from core.src.use_cases.load import Loader
from core.src.use_cases.main_view import MainView

loader: Loader = Loader()
loader.load_data_sources()
loader.load_visualizers()
mainView: MainView = MainView()


def base(request):
    context = {
        "data_sources":loader.data_sources.keys,
        "visualizers": loader.visualizers.keys
    }

    return render(request, 'index.html',context)

def show_main_view(request):
    if request.method == 'POST':
        visualizerPlugin = request.POST.get("visualizer",False)
        sourcePlugin = request.POST.get("source", False)

    if not(visualizerPlugin and sourcePlugin):
        return render(request, 'index.html',{"formInvalid":True,"data_sources":loader.data_sources.keys,
                                        "visualizers": loader.visualizers.keys})
    
    return render(request, 'index.html',{'mainView':mainView.load_main_view(sourcePlugin,visualizerPlugin,loader),
                                         "data_sources":loader.data_sources.keys,
                                        "visualizers": loader.visualizers.keys})