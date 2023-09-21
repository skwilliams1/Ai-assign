# referenced https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/ for dijkstra's algorithm

def search(graph, start, end):

    visited = set()
    path  = {start: (None, 0 )}
    current = start

    if current == end:
        print(f"Vertex {start} to vertex {end} total edge weight is 0")

    while current!= end:
        visited.add(current)
        neighbours = []
        # path = queue.pop(0)
        # node = path[-1]
        # visited.append(current)
        neighbours.append(graph[current])
        print(neighbours)
        weight_to_current = int(path[current][1])

        for neighbour in neighbours:
            print(neighbour[0])
            weight = int(neighbour[1]) + weight_to_current

            if neighbour[0] not in path:
                path[neighbour[0]] = (current, weight)

            else:
                s_weight = path[neighbour][1]
                if s_weight > weight:
                    path[neighbour] = (current, weight)
        for node in path:
            if node not in visited:
                next = {node: path[node]}
        if not next:
            print("Path does not exist")
            return
        current = min(next, key=lambda k: next[k][1])

    s_path = []
    while current is not None:
        s_path.append(current)
        next_node = path[current][0]
        current = next_node
    s_path.reverse()
    print ("The shortest path is: ")
    for i in range (0,len(s_path)-1):
        print (f"Vertex {s_path[i]} to Vertex {s_path[i+1]}")

    print(f"The total weight is {weight}")
    # for node in shortest_path:

    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    graph = {}



   # file = open("input.txt", "r")
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            data = line.split("  ")
            # print (data)

            graph[data[0]] = (data[1], data[2])


    print (graph)
    start = input("Starting Vertex: ")
    end = input("End Vertex: ")

    search(graph, start, end)










