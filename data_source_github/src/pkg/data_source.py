from github import Auth
from github import Github, NamedUser
from api.src.plugin.models.graph import *
from api.src.plugin.services.service_base import GraphLoadBase


MAX_NODES = 80
MAX_OUTER_FOR = 100
MAX_INNER_FOR = 2
auth = Auth.Token('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')
username = "amigoscode"

def add_node(namedUser: NamedUser,graph: Graph) -> Node:
    return graph.add_node({"username" : str(namedUser).split('\"')[1],
                    "email" : namedUser.email,
                    "bio" : namedUser.bio,
                    "public repos" : namedUser.public_repos,
                    "private repos" : namedUser.total_private_repos})

def add_edge(source: Node, destination: Node, graph: Graph) -> Edge:
    return graph.add_edge(source, destination)


def load_graph_from_github_api() -> Graph:
    github = Github(auth=auth)
    graph = Graph()
    user = github.get_user(username)
    followers = user.get_followers()
    userNode = add_node(user, graph)

    n: int = MAX_OUTER_FOR
    if user.followers < n:
        n = user.followers
        
    for i in range(0, n):
        if len(graph.nodes) < MAX_NODES:
            followerNode = add_node(followers[i], graph)
            add_edge(followerNode, userNode, graph)
        else:
            break

        m: int = MAX_INNER_FOR
        if followers[i].followers < m:
            m = followers[i].followers

        followerFollowers = followers[i].get_followers()
        for j in range(0, m):
            if len(graph.nodes) < MAX_NODES:
                followerFollowerNode =  add_node(followerFollowers[j], graph)
                add_edge(followerFollowerNode, followerNode, graph)
            else:
                break

        followerFollowing = followers[i].get_following()
        m = MAX_INNER_FOR
        if followers[i].following < m:
            m = followers[i].following
        for j in range(0, m):
            if len(graph.nodes) < MAX_NODES:
                followerFollowingNode = add_node(followerFollowing[j], graph)
                add_edge(followerNode, followerFollowingNode, graph)
            else:
                break

    return graph
                


class GraphLoadGithub(GraphLoadBase):
    def identifier(self):
        return "GraphLoadGithub"
    
    def name(self):
        return "Load Graph from Github API"
    
    def load_graph(self) -> Graph:
        return load_graph_from_github_api()