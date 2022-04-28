import networkx as nx
import array_to_latex as a2l
from scipy.linalg import norm 
import numpy as np
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_nodes_from([1,2,3,4,5,6])
g.add_edges_from([(1,2), (1,3), (1,4), (2,1), (2,4), (3,1), (3,4), (3,5), (4,2), (4,5),(4,6), (5,3), (5,6), (6,4)])

g0 = nx.DiGraph()
g0.add_nodes_from([1,2,3,4,5,6])
g0.add_edges_from([(1,2), (1,3), (1,4), (2,1), (2,4), (3,1), (3,4), (3,5), (4,2), (4,5),(4,6), (5,3), (5,6)])

adjacency_matrix = nx.convert_matrix.to_numpy_array(g)
row_stochastic_matrix = nx.convert_matrix.to_numpy_array(nx.stochastic_graph(g))
row_stochastic_matrix0 = nx.convert_matrix.to_numpy_array(nx.stochastic_graph(g0))

stoch = row_stochastic_matrix0 + np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1/6,1/6,1/6,1/6,1/6,1/6]])


adj = a2l.to_ltx(adjacency_matrix, frmt = '{:6.2f}', arraytype = 'array')
sto = a2l.to_ltx(row_stochastic_matrix, frmt = '{:6.2f}', arraytype = 'array')

sto0 = a2l.to_ltx(row_stochastic_matrix0, frmt = '{:6.2f}', arraytype = 'array')

#print(adj)
print(sto0)

x_prev = np.ones(6)/6
alpha = 0.01
err = []
x_next = (x_prev.T @ stoch).T
print(x_prev, x_next)
while norm(x_prev-x_next) > alpha:
    x_prev = x_next
    x_next = (x_prev.T @ stoch).T
    print(x_prev, x_next, norm(x_prev-x_next))
    err.append(norm(x_prev-x_next))
    
plt.plot(err,  color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=5)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Power Method')
plt.show()
next = a2l.to_ltx(x_next, frmt = '{:6.2f}', arraytype = 'array')
print(next, x_next.sum())
    
    


    