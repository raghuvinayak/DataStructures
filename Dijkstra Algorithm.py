



from collections import namedtuple

    


def Dijasktra(graph, start, goal):
    
    Edges = namedtuple("Edges","start, stop, cost")

    graph_data = graph.copy()

    edges_fixing = [Edges(*edge) for edge in graph_data]

    unique = (set (sum ( [[edge.start, edge.stop] for edge in edges_fixing], [])))

    vertices = {vertex: {} for vertex in unique}

    for edge in edges_fixing:

        vertices[edge.start].update({edge.stop:edge.cost})

    shortest_distance = {}
    track_predecessor = {}
    path_tracking = []
    inf = 99999
    unseen = vertices    
    
    for node in unseen:

        shortest_distance[node] = inf

    shortest_distance[start] = 0



    while unseen:

        min_distance = None

        for node in unseen:

            if min_distance is None:
                min_distance = node


            elif shortest_distance[node] < shortest_distance[min_distance]:

                min_distance = node


        path_options = unseen[min_distance].items()

        for child, weight in path_options:

            if weight + shortest_distance[min_distance] < shortest_distance[child]:

                shortest_distance[child] = weight + shortest_distance[min_distance]

                track_predecessor[child] = min_distance


        unseen.pop(min_distance)


    current_node = goal
    while current_node != start:

        try:
            path_tracking.insert(0, current_node)

            current_node = track_predecessor[current_node]
        

        except KeyError:

            print("out of range")
            break

    path_tracking.insert(0, start)

    if shortest_distance[goal] != inf:

        print("the shortest distance is  " + str(shortest_distance[goal]))

        print("the shortest path is  "  + str(path_tracking))


graph = ([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])

Dijasktra(graph, "a", "e")
           
