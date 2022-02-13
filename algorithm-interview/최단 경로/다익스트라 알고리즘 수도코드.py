"""
function Dijkstra(graph, source):
    dist[source] <- 0

    create vertex priority queue Q

    for each vertex v in graph:
        if v != source:
            dis[v] <- INF
            prev[v] <- UNDEFINED

        Q.add_with_priority(v, dist[v])

    while Q is not empty:
        u <- Q.extract_min()
        for each neighbor v of u:
            alt <- dist[u] + length(u, v)
            if alt < dist[v]:
                dist[v] <- alt
                prev[v] <- u
                Q.decrease_priority(v, alt)

    return dist, prev
"""