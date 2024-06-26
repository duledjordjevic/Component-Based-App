import requests

from api.src.plugin.models.graph import Graph
from api.src.plugin.services.service_base import GraphLoadBase


url = "https://tiktok-api15.p.rapidapi.com/index/Tiktok/getCommentListByVideo"

querystring = {
    "url": "https://www.tiktok.com/@mrbeast/video/7229017548413570350",
    "count": "50",
    "cursor": "0"
}

headers = {
	"X-RapidAPI-Key": "87b7429b0cmsh23aa368f85d73afp1e8b19jsn6078007ccadb",
	"X-RapidAPI-Host": "tiktok-api15.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)

comments_data = response.json()


MAX_REPLIES_NUMBER = 20

def add_node(text, id, graph):
    return graph.add_node({"text" : text,
                    "id" : id})

def add_edge(source, destination, graph):
    return graph.add_edge(source, destination)


def load_graph_from_tiktok_api(configuration_params:dict):

    MAX_NODES = int(configuration_params["Max nodes"])
    querystring["url"] = configuration_params["Tiktok url"]

    graph = Graph()
    nodes_size = 0
    if 'data' in comments_data and 'comments' in comments_data['data']:
        comments = comments_data['data']['comments']

        for comment in comments:
            comment_id = comment.get('id')
            comment_text = comment.get('text')

            commentNode = add_node(comment_text, comment_id, graph)
            nodes_size += 1
            if (nodes_size == MAX_NODES):
                break
            querystringReplies = {"comment_id": comment_id, "cursor": "0", "count": str(MAX_REPLIES_NUMBER)}

            urlReplies = "https://tiktok-api15.p.rapidapi.com/index/Tiktok/getReplyListByCommentId"
            headersReplies = {
                "X-RapidAPI-Key": "87b7429b0cmsh23aa368f85d73afp1e8b19jsn6078007ccadb",
                "X-RapidAPI-Host": "tiktok-api15.p.rapidapi.com"
            }
            responseReplies = requests.get(urlReplies, headers=headersReplies, params=querystringReplies)

            if responseReplies.status_code == 200:
                replies_data = responseReplies.json()

                if 'data' in replies_data and 'comments' in replies_data['data']:
                    replies = replies_data['data']['comments']
                    for reply in replies:
                        reply_text = reply.get('text')
                        replyNode = add_node(reply_text, 0, graph)
                        nodes_size += 1
                        if (nodes_size == MAX_NODES):
                            break
                        add_edge(commentNode, replyNode, graph)
            
            if (nodes_size == MAX_NODES):
                break

            
    return graph

class GraphLoadTiktok(GraphLoadBase):
    def identifier(self):
        return "GraphLoadTiktok"
    
    def name(self):
        return "Load Graph from Tiktok API"
    
    def load_graph(self, configuration_params:dict) -> Graph:
        return load_graph_from_tiktok_api(configuration_params)

    def get_configuration_params(self) -> list:
        return ["Max nodes", "Tiktok url"]