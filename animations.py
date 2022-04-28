from manim import *
import networkx as nx
import matplotlib.pyplot as plt

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  labels=True,
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()



nxgraph = nx.erdos_renyi_graph(14, 0.5)

class ImportNetworkxGraph(Scene):
    def construct(self):
        G = Graph.from_networkx(nxgraph, layout="random", layout_scale=4)
        self.play(Create(G))
        self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                         3*UP*np.sin(ind/7 * PI))
                    for ind, v in enumerate(G.vertices)])
        self.play(Uncreate(G))

#g = nx.DiGraph()
#g.add_nodes_from([1,2,3,4,5,6])
#g.add_edges_from([(1,2), (1,3), (1,4), (2,1), (2,4), (3,1), (3,4), (3,5), (4,2), (4,5),(4,6), (5,3), (5,6), (6,4)])
#subax1 = plt.subplot(121)
#nx.draw(g, with_labels=True, font_weight='bold', ax=subax1)
#plt.savefig('./images/example.jpg')

g0 = nx.DiGraph()
g0.add_nodes_from([1,2,3,4,5,6])
g0.add_edges_from([(1,2), (1,3), (1,4), (2,1), (2,4), (3,1), (3,4), (3,5), (4,2), (4,5),(4,6), (5,3), (5,6), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)])
subax = plt.subplot(111)
nx.draw(g0, with_labels=True, font_weight='bold', ax=subax)
plt.show()
#plt.savefig('./images/dangling.jpg')


class ExampleGraph(Scene):
    def construct(self):
        G = Graph.from_networkx(g, layout="circular", layout_scale=4, labels=True)
        self.play(Create(G))
        self.wait()