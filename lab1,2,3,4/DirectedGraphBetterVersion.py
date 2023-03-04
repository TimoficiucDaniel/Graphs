import copy
import math


class DirectedGraph:
    def __init__(self):
        """
        -function initiator for the graph
        -it starts out with 0 vertices and 0 edges
        - creates several dictionaries used for storing:
                ~ the vertices which have edges going out of them (origin vertice as key and destination vertices
                 as members of a list in the dictionary located at the designated key)
                ~ the vertices which have edges going into them (destination vertice as key and origin vertices
                 as members of a list in the dictionary located at the designated key)
                ~ the edges and their costs; the keys are formed out of a special format which is
                "origin_vertex_of_edge"+"_"+"destination_vertex_of_edge" and the cost is stored at the entry of the key
        """
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices_in = {}
        self.__vertices_out = {}
        self.__edges_list = {}
        self.__current_file = ""

    def initiate_for_test(self):
        """
        -a simple function that generates deepcopies of the dictionaries that store the graphs data; used for in depth
        testing ; it stores them as self parameters which arent private which allows test functions to access them
        :return:
        """
        self.test_vertices_in = copy.deepcopy(self.__vertices_in)
        self.test_vertices_out = copy.deepcopy(self.__vertices_out)
        self.test_edges_list = copy.deepcopy(self.__edges_list)

    def read_from_file(self, filename):
        """
        -a function that reads a graph from a file and stores its data into the object entity
        -it first opens the file with a certain filename and it reads the first line containing the
        number of vertices and number of edges
        -it clears up any old data from a previous graph and generates the necessary keys (origin and destination
        vertices for the dictionaries that contain the vertices which have edges going out of them or into them) which
        take values from 0 to the number_of_vertices - 1
        -it then reads the textfile line by line , splitting it into 3 parameters , origin vertex, destination vertex
        and cost of the edge ;it then adds the corresponding data to the dictionaries (until all edges = number of lines
        in textfile - 1 are read)
        -it then stores the filename as a parameter of the entity and closes the file
        :param filename:
        :return:
        """
        f = open(filename, "rt")
        first_line = f.readline().strip()
        self.__number_of_vertices, self.__number_of_edges = first_line.split()
        self.__vertices_in.clear()
        self.__vertices_out.clear()
        self.__edges_list.clear()
        for i in range(int(self.__number_of_vertices)):
            self.__vertices_in[str(i)] = []
            self.__vertices_out[str(i)] = []
        for i in range(int(self.__number_of_edges)):
            line = f.readline().strip()
            vertice_list = line.split()
            self.__vertices_in[vertice_list[1]].append(vertice_list[0])
            self.__vertices_out[vertice_list[0]].append(vertice_list[1])
            self.__edges_list[str(vertice_list[0]) + "_" + str(vertice_list[1])] = vertice_list[2]
        self.__current_file = filename
        f.close()

    def write_to_file(self, filename):
        """
        -a function that takes the current graph stored in the object and saves it into a file with a certain given name
        -it uses the dictionary of vertices that have edges going out of them to write to the file the edges and their
        costs
        -it saves it in the right format so the file can be read again by the same object
        :param filename:
        :return:
        """
        f = open(filename, "wt")
        f.write(str(self.__number_of_vertices) + " " + str(self.__number_of_edges) + "\n")
        for origins in self.__vertices_out.keys():
            if len(self.__vertices_out[origins]) > 0:
                for destinations in self.__vertices_out[origins]:
                    f.write(origins + " " + destinations + " " + self.__edges_list[origins + "_" + destinations] + "\n")
        f.close()

    @property
    def current_file(self):
        """
        getter which returns the current file - used by ui function to save current file
        :return:
        """
        return self.__current_file

    @property
    def number_of_vertices(self):
        """
        getter which returns the number of vertices
        O(1) time complexity
        :return:
        """
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        """
        getter which returns the number of edges
        O(1) time complexity
        :return:
        """
        return self.__number_of_edges

    def get_cost(self, origin, destination):
        """
        -function that returns the cost of an edge
        -raises error if edge does not exist
        O(1) complexity since it executes just one return , no loops or anything
        :param origin: vertex
        :param destination: vertex
        :return:
        """
        if origin + "_" + destination not in self.__edges_list.keys():
            raise ValueError("Edge does not exist!")
        return self.__edges_list[origin + "_" + destination]

    def set_cost(self, origin, destination, value):
        """
        -function that sets/updates the cost of an edge
        -raises error if: origin == destination; if origin vertex does not exist
        if destination vertex does not exist , if cost is not a numeric value
        or if edge does not exist
        -O(1) time complexity
        :param origin: vertex
        :param destination: vertex
        :param value:
        :return:
        """
        if origin == destination:
            raise ValueError("Cannot draw an edge from a point to itself!")
        if origin not in self.__vertices_out.keys():
            raise ValueError("Origin vertice does not exist!")
        if destination not in self.__vertices_in.keys():
            raise ValueError("Destination vertice does not exist!")
        if value.isnumeric() is False:
            raise ValueError("Cost has to be a numeric value!")
        if origin + "_" + destination not in self.__edges_list.keys():
            raise ValueError("Edge does not exist!")
        self.__edges_list[origin + "_" + destination] = value

    def add_vertice(self, vertice):
        """
        -function that adds a new vertex to the graph
        -raises error if vertex already in graph
        -increments number of vertices and creates the keys and lists in the dictionaries for the vertex
        O(1) time complexity
        :param vertice:
        :return:
        """
        if vertice in self.__vertices_in.keys():
            raise ValueError("Vertice already in !")
        self.__vertices_in[vertice] = []
        self.__vertices_out[vertice] = []
        self.__number_of_vertices = str(int(self.__number_of_vertices) + 1)

    def add_edge(self, origin, destination, cost):
        """
        -function that adds en edge to the graph
        -raises error if :origin == destination ; if origin vertex does not exist; if destination vertex
        does not exist, if cost is not a numeric value
        -append the origin and destination vertices to the dictionaries accordingly
        -creates a new key for the edge dictionary using the specified format and assigns it the cost
        O(1) time complexity
        :param origin: vertex
        :param destination: vertex
        :param cost:
        :return:
        """
        if origin == destination:
            raise ValueError("Cannot draw an edge from a point to itself!")
        if origin not in self.__vertices_out.keys():
            raise ValueError("Origin vertice does not exist!")
        if destination not in self.__vertices_in.keys():
            raise ValueError("Destination vertice does not exist!")
        if cost.isnumeric() is False:
            raise ValueError("Cost has to be a numeric value!")
        self.__edges_list[origin + "_" + destination] = cost
        self.__vertices_in[destination].append(origin)
        self.__vertices_out[origin].append(destination)
        self.__number_of_edges = str(int(self.__number_of_edges) + 1)

    def remove_edge(self, origin, destination):
        """
        -function that removes an edge
        -removes the origin vertex from list of in_vertices in the dictionary with vertices that have edges going into
        them
        -removes the destination vertex from list of out out_vertices in the dictionary with vertices that have edges
        going out of them
        -deletes the edge and the key from the dictionary
        -raises error if origin vertex does not exist; if destination vertex does not exist or if edge does not exist
        O(1) time complexity
        :param origin:
        :param destination:
        :return:
        """
        if origin not in self.__vertices_out.keys():
            raise ValueError("Origin vertice does not exist!")
        if destination not in self.__vertices_in.keys():
            raise ValueError("Destination vertice does not exist!")
        if origin + "_" + destination not in self.__edges_list.keys():
            raise ValueError("Edge does not exist!")
        self.__edges_list.pop(origin + "_" + destination)
        self.__number_of_edges = str(int(self.__number_of_edges) - 1)
        self.__vertices_in[destination].remove(origin)
        self.__vertices_out[origin].remove(destination)

    def remove_vertice(self, vertice):
        """
        -function that removes a vertice
        -removes it from both dictionaries (both the key and the corresponding lists)
         along with all the edges which contain this respective vertex
         -raises error if vertex to be removed does not exist
         O(1) complexity
        :param vertice:
        :return:
        """
        if vertice not in self.__vertices_out.keys():
            raise ValueError("Vertice does not exist!")
        for destinations in self.__vertices_out[vertice]:
            self.__edges_list.pop(vertice + "_" + destinations)
            self.__number_of_edges = str(int(self.__number_of_edges) - 1)
        self.__vertices_out.pop(vertice)
        for origins in self.__vertices_in[vertice]:
            self.__edges_list.pop(origins + "_" + vertice)
            self.__number_of_edges = str(int(self.__number_of_edges) - 1)
        self.__vertices_in.pop(vertice)
        self.__number_of_vertices = str(int(self.__number_of_vertices) - 1)

    def check_edge(self, origin, destination):
        """
        -function that checks if an edge exists using the specified format to search among the
        keys of the edges list ; if edge_format is in dictionary keys return true
        otherwise false
        O(1) complexity (I am not sure how the in statement works in python time complexity wise when its about
        finding a certain element in the list)
        :param origin:
        :param destination:
        :return:
        """
        if origin + "_" + destination in self.__edges_list.keys():
            return True
        return False

    def get_in_degree(self, vertice):
        """
        -function that returns the length of the list associated with the vertex key in the dictionary that contains
        edges going into them
        -raises error if vertex does not exist
        O(1) time complexity
        :param vertice:
        :return:
        """
        if vertice not in self.__vertices_in.keys():
            raise ValueError("Vertice does not exist!")
        return len(self.__vertices_in[vertice])

    def get_out_degree(self, vertice):
        """
         -function that returns the length of the list associated with the vertex key in the dictionary that contains
        edges going out of them
        -raises error if vertex does not exist
        O(1) time complexity
        :param vertice:
        :return:
        """
        if vertice not in self.__vertices_out.keys():
            raise ValueError("Vertice does not exist!")
        return len(self.__vertices_out[vertice])

    def copy(self):
        """
        -function that copies the current graph by first saving the current file, then writing the current graph into
        a copy.txt copy file and then loading the copy file
        -working on a copy of a graph will not modify the original graph
        :return:
        """
        self.write_to_file(self.current_file)
        self.write_to_file("copy.txt")
        self.read_from_file("copy.txt")

    def parse_inbound(self, vertice):
        """
        -function used to parse through the inbound edges of a vertex
        -raises error if vertex does not exist
        -used yield statement to be able to efficiently parse through it
        O(1) time complexity
        :param vertice:
        :return:
        """
        if vertice not in self.__vertices_in.keys():
            raise ValueError("Vertice does not exist!")
        for vertices in self.__vertices_in[vertice]:
            yield vertices

    def parse_outbound(self, vertice):
        """
        -function used to parse through the outbound edges of a vertex
        -raises error if vertex does not exist
        -used yield statement to be able to efficiently parse through it
        O(1) time complexity
        :param vertice:
        :return:
        """
        if vertice not in self.__vertices_out.keys():
            raise ValueError("Vertice does not exist!")
        for vertices in self.__vertices_out[vertice]:
            yield vertices

    def parse_vertices(self):
        """
        -function used to parse through all the vertices and their outbound edges of
        a graph , essentially printing line by line the format of the graph textfile
        -raises error if vertex does not exist
        -used yield statement to be able to efficiently parse through it
        O(1) time complexity to iterate
        :return:
        """
        for key in self.__vertices_out.keys():
            for vertices in self.__vertices_out[key]:
                yield key + " " + vertices

    def breadth_first_search(self, start, end):
        """
        -function which finds the shortest path from a vertix to another
        -creates a list which contain multiple paths which themselves are created as we advance through the
        -vertices(when we get to a new vertice we input all new possible paths which spring from it at the beginning
        -of the list)
        -if the current vertice is the end vertice we are looking for we return the path
        -keeps track of visited vertices and if no path is found returns no path message
         """
        list_of_paths = [[start]]
        visited = [False] * (int(self.__number_of_vertices) + 1)
        while list_of_paths:
            list_of_vertices = list_of_paths.pop(0)
            vertice = list_of_vertices[-1]
            if vertice == end:
                new_list = []
                for lists in list_of_vertices:
                    new_list.append(lists)
                return new_list
            visited[int(vertice)] = True
            for adjacent in self.__vertices_in[vertice]:
                if not visited[int(adjacent)]:
                    new_list = list(list_of_vertices)
                    new_list.append(adjacent)
                    list_of_paths.append(new_list)
        return "No path found."

    def Belford(self, vertice1, vertice2):
        """
        Complexity Theta(n^2)x i think
        Algorithm receives two vertices as parameters , one being the starting vertice and one being the destination
         vertice ;  it works in 3 steps;
         first step- initialization where the algorithm creates two dictionaries , one containing distances(infinity
          if the key vertice is not the source and 0 if it is the source) and one containing vertices that come before
          the one located at the key
          step two- relaxation where we repeatedly approximate the lowest cost of the walk between the starting vertice
          and all the other vertices in the graph until we reach the final result
          step three- we return the distance located at key of destination vertice in the distance dictionary
        :param vertice1:
        :param vertice2:
        :return:
        """
        dist = dict()
        prev = dict()
        for vertices in self.__vertices_in.keys():
            dist[vertices] = math.inf
        dist[vertice1] = 0
        for k in range(int(self.number_of_vertices) - 1):
            for edges in self.__edges_list.keys():
                x, y = edges.split("_")
                if dist[y] > dist[x] + int(self.__edges_list[edges]):
                    dist[y] = dist[x] + int(self.__edges_list[edges])
                    prev[y] = x
        return dist[vertice2]

    def topological_ordering_to_find_if_DAG(self):
        L = dict()
        vertices_in = copy.deepcopy(self.__vertices_in)
        vertices_out = copy.deepcopy(self.__vertices_out)
        ok = True
        while len(vertices_in) != 0 and ok is True:
            ok = False
            for vertice in vertices_in.keys():
                if len(vertices_in[vertice]) == 0:
                    ok = True
                    for vertice2 in vertices_out[vertice]:
                        vertices_in[vertice2].remove(vertice)
                    L[vertice] = list()
                    auxiliary_vertice = vertice
                    break
            if ok is True:
                vertices_in.pop(auxiliary_vertice)
                vertices_out.pop(auxiliary_vertice)
        if len(vertices_in) == 0:
            return True
        return False

    def depth_first_traversal(self):
        """
        function returns the graph sorted in topological order if its a Directed acyclic graph based on BFS;
        it creates a:
         -list ( representing the future sorted graph )
         -a set ( representing the vertices which are being processed )
         -another set ( representing the vertices which were processed )
         -it goes through each vertex and if it has not been processed it calls a sub-algorithm which checks for
         cycles and marks vertices as processed
         if it detects a cycle it returns None
         it then returns the sorted list
        :return:
        """
        sorted_list = list()
        fully_processed = set()
        in_process = set()
        for vertice in self.__vertices_in.keys():
            if vertice not in fully_processed:
                ok = self.topo_sort_dfs(vertice, sorted_list, fully_processed, in_process)
                if not ok:
                    sorted_list = None
                    return sorted_list
        return sorted_list

    def topo_sort_dfs(self, vertice, sorted_list, fully_processed, in_process):
        """
        sub-algorithm which checks for cycles and marks vertices as processed
        - it goes through every inbound vertex of the vertice given as a parameter
        - if it that inbound vertex is already processed then it means that there is a cycle at which point
        it returns False and cancels the algorithm
        - if it has not been processed it calls this function recursively with parameter = the new vertex
        if it reached the end of a branch it starts removing all processed vertices from the in_process list and
        appends it to processed list and adds it to the list in topological order
        :param vertice:
        :param sorted_list:
        :param fully_processed:
        :param in_process:
        :return:
        """
        in_process.add(vertice)
        for vertice_2 in self.__vertices_in[vertice]:
            if vertice_2 in in_process:
                return False
            else:
                if vertice_2 not in fully_processed:
                    ok = self.topo_sort_dfs(vertice_2, sorted_list, fully_processed, in_process)
                    if not ok:
                        return False
        in_process.remove(vertice)
        sorted_list.append(vertice)
        fully_processed.add(vertice)
        return True

    def find_highest_cost_path(self, destination):
        """
        algorithm gets the highest cost path from the root vertex of the DAG to a destination vertex
        -works only if its a DAG
        it works on a list sorted in topological order by the previous BFS - based algorithm and on the principle of
        relaxation
        Step 1: it creates a distances dictionary in which we store distances and if the key is not equal to the root we
         set it to -infinity or 0 if it is the root
        Step 2: we go through the topological order list and then for each of these vertices we parse through their
         outbound edges
        Step 3: we relax the edges by comparing the distance[this vertex] to the distance from the root to the previous
        inbound vertex + the cost of the edge from the previous vertex to this one ; if distance[this vertex] is smaller
        than the mathematical equation then we set distance[this vertex] to be equal to that
        Step 4: return the distance to that requested vertex
        :param destination:
        :return:
        """
        topo_list = self.depth_first_traversal()
        if topo_list is None:
            return "It is not a DAG so cannot perform operation"
        dist = dict()
        for vertices in topo_list:
            dist[vertices] = -math.inf
        dist[topo_list[0]] = 0
        for i in range(len(topo_list)):
            if topo_list[i] == destination:
                break
            for out_vertices in self.__vertices_out[str(i)]:
                if dist[out_vertices]<(dist[str(i)])+int(self.__edges_list[str(i) + "_" + out_vertices]):
                    dist[out_vertices] = (dist[str(i)]) + int(self.__edges_list[str(i) + "_" + out_vertices])
        return dist[destination]

