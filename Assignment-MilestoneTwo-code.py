import math
def create_graph_list_from_file():
    a = open('Assignment-MilestoneTwo-doc.txt')
    numvert = int(a.readline().strip()) 
    numedge = a.readlines()
    a.close()
    graph_list = [[0 for _ in range(numvert)] for _ in range(numvert)]
    for item in numedge:
        item = item.strip() 
        item_list = item.split()
        if len(item_list) != 3:
            continue
        rows = int(item_list[0])
        cols = int(item_list[1])
        dis = int(item_list[2])
        graph_list[rows][cols] = dis 
        graph_list[cols][rows] = dis 
    # End for
    return graph_list
#End def
def way_travel(list_previous_vert, end_point):
    list = [end_point]
    vert = end_point
    while True:
        vert = list_previous_vert[vert]
        if vert == None: 
            break
        # End if
        list.insert(0, vert)
    # End while
    list = [str(x) for x in list]
    return '->'.join(list)
# End def
def shortest_way(list_dis, list_shortest_way):
    min_way = math.inf 
    for vert in range(len(list_dis)):
        if (list_dis[vert] < min_way and list_shortest_way[vert] == False):
            min_way = list_dis[vert]
            min_vert = vert
        # End if
    # End for
    return min_vert
# End def
def shortest_path(graph, str_point):
    numvert = len(graph)
    list_dis = [math.inf] * numvert 
    list_dis[str_point] = 0 
    list_shortest_way = [False] * numvert 
    list_previous_way = [None] * numvert  
    for i in range(numvert):
        x = shortest_way(list_dis, list_shortest_way)
        list_shortest_way[x] = True
        for y in range(numvert):
            if graph[x][y] > 0 and list_shortest_way[y] == False and list_dis[y] > list_dis[x] + graph[x][y]:
                list_dis[y] = list_dis[x] + graph[x][y]
                list_previous_way[y] = x
            # End if
        # End for
    # End for              
    list_min_way=[]
    for end_point in range(numvert):
        output = str(end_point) + " : "
        output += way_travel(list_previous_way, end_point) + " : "
        output += str(list_dis[end_point])
        print(output)
        list_min_way.append(list_dis[end_point])
    # End for   
    return list_min_way
# End def
def optimum_way(numvert, list_min_way, unvisited_list, optimum_way_list):
    for i in range(numvert):
        if list_min_way[i] == 0:
            list_min_way[i] = math.inf
        elif i in optimum_way_list:
            list_min_way[i] = math.inf
    end_point = list_min_way.index(min(list_min_way))
    unvisited_list.remove(end_point)
    optimum_way_list.append(end_point)
    return optimum_way_list
def main():
    graph = create_graph_list_from_file()
    unvisited_list = []
    for i in range(len(graph)):
        unvisited_list.append(i)
    unvisited_list.pop(0)
    optimum_way_list = [0]
    for i in range(len(graph)-1):
        print("Start : " + str(optimum_way_list[-1]))
        optimum_way(len(graph), shortest_path(graph, optimum_way_list[-1]), unvisited_list, optimum_way_list)
        print("*********")
    # End for
    print("Start : " + str(optimum_way_list[-1]))
    shortest_path(graph, optimum_way_list[-1])
    print("*********")
    optimum_list = []
    optimum_list = [str(x) for x in optimum_way_list]
    way = " -> ".join(optimum_list)
    print("Optimum way: " + way)
# End def
if __name__ == '__main__':
    main()
# End if