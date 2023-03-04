class Graph:
    def __init__(self):
        self.vertices = dict()
        self.edges = dict()

    def tsp(self):
        for vertex in self.vertices.keys():
            x = vertex
            currentCycle = [x]
            over = False
            sortedEdges = sorted(self.edges, key=lambda y: self.edges[y])

            while not over and len(currentCycle) <= len(self.vertices.keys()):
                over = True

                firstFiltered = []
                for i in sortedEdges:
                    if i[0] == x:
                        found = True
                        for elements in currentCycle:
                            if elements != currentCycle[0] and i[1] in elements:
                                found = False
                        if found is True:
                            firstFiltered.append(i)

                if len(firstFiltered) > 0:
                    z = firstFiltered[0]
                    over = False

                if not over:
                    currentCycle.append(z)
                    x = z[1]

                if len(currentCycle) == len(self.vertices.keys()):
                    if self.existsEdge(currentCycle[0], currentCycle[-1][1]):
                        currentCycle.append((currentCycle[-1][1], currentCycle[0]))
                        return currentCycle

    def existsEdge(self, param, param1):
        if (param1, param) in self.edges.keys():
            return True
        return False
