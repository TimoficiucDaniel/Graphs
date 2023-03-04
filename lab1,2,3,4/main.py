
"""
graph2 = DirectedGraph()
graph2.read_from_file("graph1k.txt")

graph2.write_to_file("test2.txt")

"""
from Ui import Ui
from DirectedGraphBetterVersion import DirectedGraph

graph = DirectedGraph()
graph.read_from_file("graphDAG.txt")
ui = Ui(graph)
ui.startUi()