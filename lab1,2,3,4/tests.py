import unittest

from DirectedGraphBetterVersion import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.testGraph = DirectedGraph()
        self.testGraph.read_from_file("testfile.txt")

    def testGraph(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertEqual(self.testGraph.number_of_vertices, "1000")
        self.assertEqual(self.testGraph.number_of_edges, "4000")

    def test_set_cost(self):
        self.testGraph.read_from_file("testfile.txt")
        self.testGraph.set_cost("0", "154", "2000")
        self.testGraph.initiate_for_test()
        self.assertEqual(self.testGraph.test_edges_list["0_154"], "2000")
        self.assertRaises(ValueError, self.testGraph.set_cost, "0", "0", "200")
        self.assertRaises(ValueError, self.testGraph.set_cost, "1001", "154", "200")
        self.assertRaises(ValueError, self.testGraph.set_cost, "100", "1540", "200")
        self.assertRaises(ValueError, self.testGraph.set_cost, "0", "154", "str")
        self.assertRaises(ValueError, self.testGraph.set_cost, "0", "2", "100")

    def test_add_vertice(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError,self.testGraph.add_vertice,"100")
        self.testGraph.add_vertice("1001")
        self.testGraph.initiate_for_test()
        self.assertEqual(self.testGraph.test_vertices_in["1001"], [])
        self.assertEqual(self.testGraph.test_vertices_out["1001"], [])
        self.assertEqual(self.testGraph.number_of_vertices , "1001")

    def test_remove_vertice(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError,self.testGraph.remove_vertice,"1002")
        self.testGraph.remove_vertice("0")
        self.assertEqual(self.testGraph.number_of_vertices,"999")
        self.assertEqual(self.testGraph.number_of_edges,"3989")

    def test_add_edge(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError, self.testGraph.add_edge,"0","0","200")
        self.assertRaises(ValueError, self.testGraph.add_edge, "1003", "0", "200")
        self.assertRaises(ValueError, self.testGraph.add_edge, "0", "1003", "200")
        self.assertRaises(ValueError, self.testGraph.add_edge, "0", "2", "str")
        self.testGraph.add_edge("0","2","200")
        self.testGraph.initiate_for_test()
        self.assertEqual(self.testGraph.test_vertices_out["0"][-1],"2")
        self.assertEqual(self.testGraph.test_vertices_in["2"][-1],"0")
        self.assertEqual(self.testGraph.test_edges_list["0_2"],"200")
        self.assertEqual(self.testGraph.number_of_edges,"4001")

    def test_remove_edge(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError, self.testGraph.remove_edge, "1005", "2")
        self.assertRaises(ValueError, self.testGraph.remove_edge, "12", "2000")
        self.assertRaises(ValueError, self.testGraph.remove_edge, "0", "2")
        self.testGraph.remove_edge("0","154")
        self.testGraph.initiate_for_test()
        self.assertEqual(self.testGraph.number_of_edges,"3999")


    def test_check_edge(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertTrue(self.testGraph.check_edge("0","154"))
        self.assertFalse(self.testGraph.check_edge("0","153"))

    def test_get_in_degree(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError,self.testGraph.get_in_degree,"1005")
        self.assertEqual(self.testGraph.get_in_degree("0"),4)


    def test_get_out_degree(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertRaises(ValueError,self.testGraph.get_out_degree,"1005")
        self.assertEqual(self.testGraph.get_out_degree("0"),7)

    def test_current_file(self):
        self.testGraph.read_from_file("testfile.txt")
        self.assertEqual(self.testGraph.current_file,"testfile.txt")

    def tearDown(self):
        self.testGraph = None
