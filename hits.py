import numpy as np                                                              #importing numpy for linear algebra of matrices
import scipy.sparse                                                      	#scipy for sparse matrix representation
from networkx.exception import NetworkXError
arr = np.loadtxt("elec.txt")          						#loading data that has edge(out) and edge(in), weight 								
arr = np.delete(arr, 3, axis=1)							#timestamp
shape = tuple(arr.max(axis=0)[:2]+1)
coo = scipy.sparse.coo_matrix((arr[:, 2], (arr[:, 0], arr[:, 1])), shape=shape, #deleting timestamp for now
                        dtype=arr.dtype)
print(coo.todense())								#convert to sparse matrix

it = 100
tol=1.0e-6 									#define tolerence
(n,m)=coo.shape
print n
print m										#verify square matrix
A=coo.T*coo
x=scipy.ones((n,1))/n								#initialize authority to all 1s
for i in range(it):
        xprev=x
        x=A*x
        x=x/x.sum()								#multiply with adjacency matrix and itself        
        err=scipy.absolute(x-xprev).sum()
        if err < n*tol:								#power iteration
            a=np.asarray(x).flatten()
            h=np.asarray(coo*a).flatten()
            h/=h.sum()								#alter hubs and authorities values
rh = np.sort(h)[-10:][::-1]
ra = np.sort(a)[-10:][::-1]
print "The hubs and authorities values ranked:"
print rh									#sort top 10
print ra


h = h.argsort()[-10:][::-1]							#retrieve indices of top 10
a = a.argsort()[-10:][::-1]
l = np.vstack([h,a])
l = np.reshape(l, 20)
print "The top 10 hubs are:"
print h
print "The top 10 authorities are:"
print a
lh=np.array(h).tolist()
la=np.array(a).tolist()
lrh=np.array(854311*rh).tolist()						#prepare an size list for plotting later which correlates to rank obtained
lra=np.array(5554311*ra).tolist()


import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()									#create a directed graph using networkx and add all the edges
G.add_weighted_edges_from(arr)


A = G.subgraph(l)
pos=nx.shell_layout(A)								#prepare a subgraph of the top hubs and authorities nodes


nx.draw_networkx_nodes(A,pos,
                       nodelist=np.array(h).tolist(),				#draw hubs seperately in blue
                       node_color='blue',
                       node_size=lrh,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,							#draw authorities seperately in green
                       nodelist=np.array(a).tolist(),
                       node_color='green',
                       node_size=lra,
                   alpha=0.8)
nx.draw_networkx_edges(A, pos, width=1, alpha=0.3, edge_color='blue')
nx.draw_networkx_labels(A, pos, font_size=12, font_family='sans-serif')
plt.show()


