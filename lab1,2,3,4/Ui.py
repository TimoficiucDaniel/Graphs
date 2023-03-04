import random


class Ui:
    def __init__(self, graph):
        """
        class initiator for ui which defines two attributes: a graph and a list of predefined file names used to load
        predefined graphs given in the problem statement
        :param graph: the directed graph which will be attributed to the graph attribute
        """
        self.__graph = graph
        self.__file_list = ["graph1k.txt", "graph10k.txt", "graph100k.txt", "graph1m.txt","graphDAG.txt"]

    def generate_graph(self, number_of_vertices, number_of_edges):
        """
        -an external function which takes in to parameters which are manually given by the user , them being the number
        of vertices and edges used to generate a random graph
        -the function creates an empty dictionary which is used later to generate a random.txt file that contains are our
        random graph
        -the function then generates edges of the format "origin_vertex"+"_"+"destination vertex"
         using the predefined random.randint function which takes value from 0 to number_of_vertices - 1
         -the function generates another destination if the origin and destination vertexes are the same or if the given
         edge already exists as a key in the dictionary
         -the function also attributes the edges a random cost between 0 and 100
         -then using the dictionary keys ,which are ordered alphabetically ,the function writes to the random.txt file
         the graph in the correct format
         -it also stores the random.txt file into the file_list so it can be loaded up by the program later
        :param number_of_vertices:
        :param number_of_edges:
        :return:
        """
        graph_dict = dict()
        og_vertices = number_of_vertices
        og_edges = number_of_edges
        while number_of_edges > 0:
            a = random.randint(0, number_of_vertices - 1)
            b = random.randint(0, number_of_vertices - 1)
            while a == b:
                b = random.randint(0, (number_of_vertices - 1))
            while str(a) + "_" + str(b) in graph_dict.keys():
                b = random.randint(0, (number_of_vertices - 1))
            graph_dict[str(a) + "_" + str(b)] = random.randint(0, 100)
            number_of_edges -= 1
        f = open("random.txt", "wt")
        f.write(str(og_vertices) + " " + str(og_edges) + "\n")
        for keys in sorted(graph_dict.keys()):
            cost = graph_dict[keys]
            origin, destination = keys.split("_")
            f.write(origin + " " + destination + " " + str(cost) + "\n")
        self.__file_list.append("random.txt")
        f.close()

    @staticmethod
    def show_menu():
        """
        a function that just prints out the 19 different options that the user can choose
        :return:
        """
        print("0 - number of edges")
        print("1 - get number of vertices")
        print("2 - find out if an edge exists")
        print("3 - get the in degree of a vertex")
        print("4 - get the out degree of a vertex")
        print("5 - get cost of an edge")
        print("6 - set cost of an edge")
        print("7 - add edge")
        print("8 - add vertex")
        print("9 - remove edge")
        print("10 - remove vertex")
        print("11 - copy file and load copy")
        print("12 - save file")
        print("13 - load another file")
        print("14 - parse vertices")
        print("15 - parse inbound edges of a vertex")
        print("16 - parse outbound edges of a vertex")
        print("17 - generate random graph")
        print("18 - backwards breadth first search")
        print("19 - get lowest cost walk from x to y")
        print("20 - check if graph is DAG")
        print("21 - find highest cost path")
        print("22 - exit")

    def startUi(self):
        """
        -main function of the program that lets the user choose an option to execute
        -prints out the menu before each command
        -for functions that ask for additional parameters it also reads those parameters as strings(most of the time)
        -also catches errors raised by modifying the graph in illegal ways
        -allows user to parse vertices one by one in neat way(imo)
        -prints out invalid input in case of invalid input
        :return:
        """
        while True:
            try:
                self.show_menu()
                option = input("Select command").strip()
                if option == '0':
                    print(self.__graph.number_of_edges)
                elif option == '1':
                    print(self.__graph.number_of_vertices)
                elif option == '2':
                    origin = str(input("Origin vertex:"))
                    destination = str(input("Destination vertex:"))
                    print(self.__graph.check_edge(origin, destination))
                elif option == '3':
                    vertex = str(input("Vertex:"))
                    print(self.__graph.get_in_degree(vertex))
                elif option == '4':
                    vertex = str(input("Vertex:"))
                    print(self.__graph.get_out_degree(vertex))
                elif option == '5':
                    origin = str(input("Origin vertex:"))
                    destination = str(input("Destination vertex:"))
                    print(self.__graph.get_cost(origin, destination))
                elif option == '6':
                    origin = str(input("Origin vertex:"))
                    destination = str(input("Destination vertex:"))
                    value = str(input("New cost:"))
                    self.__graph.set_cost(origin, destination, value)
                elif option == '7':
                    origin = str(input("Origin vertex:"))
                    destination = str(input("Destination vertex:"))
                    value = str(input("Cost:"))
                    self.__graph.add_edge(origin, destination, value)
                elif option == '8':
                    vertex = str(input("Vertex:"))
                    self.__graph.add_vertice(vertex)
                elif option == '9':
                    origin = str(input("Origin vertex:"))
                    destination = str(input("Destination vertex:"))
                    self.__graph.remove_edge(origin, destination)
                elif option == '10':
                    vertex = str(input("Vertex:"))
                    self.__graph.remove_vertice(vertex)
                elif option == '11':
                    self.__graph.copy()
                    self.__file_list.append(self.__graph.current_file)
                elif option == '12':
                    self.__graph.write_to_file(self.__graph.current_file)
                elif option == '13':
                    for files in self.__file_list:
                        print(files)
                    option = str(input("Choose file:"))
                    if option in self.__file_list:
                        self.__graph.read_from_file(option)
                elif option == '14':
                    ok = True
                    for x in self.__graph.parse_vertices():
                        print(x)
                        choice = str(input("1 to continue 0 to stop"))
                        if choice == '0':
                            ok = False
                        if ok is False:
                            break
                elif option == '15':
                    ok = True
                    vertex = str(input("Vertex:"))
                    for x in self.__graph.parse_inbound(vertex):
                        print(x)
                        choice = str(input("1 to continue 0 to stop"))
                        if choice == '0':
                            ok = False
                        if ok is False:
                            break
                elif option == '16':
                    ok = True
                    vertex = str(input("Vertex:"))
                    for x in self.__graph.parse_outbound(vertex):
                        print(x)
                        choice = str(input("1 to continue 0 to stop"))
                        if choice == '0':
                            ok = False
                        if ok is False:
                            break
                elif option == '17':
                    vertices = int(input("Number of vertices:"))
                    edges = int(input("Number of edges"))
                    self.generate_graph(vertices, edges)
                elif option == '18':
                    vertice_1 = str(input("Start vertix: "))
                    vertice_2 = str(input("End vertix: "))
                    print(self.__graph.breadth_first_search(vertice_1,vertice_2))
                elif option == '19':
                    vertice_1 = str(input("Start vertix: "))
                    vertice_2 = str(input("End vertix: "))
                    print(self.__graph.Belford(vertice_1,vertice_2))
                elif option == '20':
                    #print(self.__graph.topological_ordering_to_find_if_DAG())
                    print(self.__graph.depth_first_traversal())
                elif option == '21':
                    vertice = str(input("Destination vertex"))
                    print(self.__graph.find_highest_cost_path(vertice))
                elif option == '22':
                    return
                else:
                    print("invalid input")
            except ValueError as ve:
                print(str(ve))
