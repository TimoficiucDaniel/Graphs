import Lab5


def main():
    g = Lab5.Graph()
    g.vertices[1] = [2, 3, 4]
    g.vertices[2] = [1, 3, 5]
    g.vertices[3] = [1, 2, 4, 5]
    g.vertices[4] = [1, 3, 5, 6]
    g.vertices[5] = [2, 3, 4, 6]
    g.vertices[6] = [4, 5]
    g.edges[(1, 2)] = 3
    g.edges[(1, 3)] = 4
    g.edges[(1, 4)] = 5
    g.edges[(2, 1)] = 3
    g.edges[(2, 3)] = 6
    g.edges[(2, 5)] = 8
    g.edges[(3, 1)] = 4
    g.edges[(3, 2)] = 6
    g.edges[(3, 4)] = 9
    g.edges[(3, 5)] = 1
    g.edges[(4, 1)] = 5
    g.edges[(4, 3)] = 9
    g.edges[(4, 5)] = 10
    g.edges[(4, 6)] = 2
    g.edges[(5, 2)] = 8
    g.edges[(5, 3)] = 1
    g.edges[(5, 4)] = 10
    g.edges[(5, 6)] = 9
    g.edges[(6, 4)] = 2
    g.edges[(6, 5)] = 9
    print(g.tsp())

main()
