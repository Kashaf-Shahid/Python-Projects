from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from django.views import GraphAdjList, dfs, bfs

@csrf_exempt
def graph_dfs_view(request):
    vertices = 5
    graph = GraphAdjList(vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

 
    dfs_result = []
    dfs(graph.get_graph(), 0, visited=set())
    
    return JsonResponse({'DFS Traversal': dfs_result})

@csrf_exempt
def graph_bfs_view(request):
    vertices = 5
    graph = GraphAdjList(vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    bfs_result = []
    bfs(graph.get_graph(), 0)
    
    return JsonResponse({'BFS Traversal': bfs_result})