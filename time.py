import numpy as np
import scipy.sparse
from networkx.exception import NetworkXError
arr = np.loadtxt("elec.txt")							#load file into two arrays
ax = np.loadtxt("elec.txt")
arr = np.delete(arr, 3, axis=1)
ax = np.delete(ax, 2, axis=1)							#another array is used to construct the matrix required for aging the documents
shape = tuple(arr.max(axis=0)[:2]+1)
coo = scipy.sparse.coo_matrix((arr[:, 2], (arr[:, 0], arr[:, 1])), shape=shape,
                        dtype=arr.dtype)
print(coo.todense())


shape = tuple(ax.max(axis=0)[:2]+1)
cop = scipy.sparse.coo_matrix((ax[:, 2], (ax[:, 0], ax[:, 1])), shape=shape,	#build sparse matrix for both
                        dtype=arr.dtype)
cop = 1199579101*coo - cop
										#apply the formula to the timestamp matrix


it = 100
tol=1.0e-6
(n,m)=coo.shape
(n1,m1) = cop.shape
print n
print m
C=coo.T*coo
B = cop.T*cop									#this matrix is multiplied with the overall metric
A = C*B
x=scipy.ones((n,1))/n
for i in range(it):
        xprev=x
        x=A*x
        x=x/x.sum()
	err=scipy.absolute(x-xprev).sum()					#repeat same for this: power iteration
        if err < n*tol:
            a=np.asarray(x).flatten()
            h=np.asarray(coo*a).flatten()
            h/=h.sum()

rh = np.sort(h)[-10:][::-1]
ra = np.sort(a)[-10:][::-1]
print "The ranked values of hubs and authorities respectively:"
print rh
print ra


h = h.argsort()[-10:][::-1]
a = a.argsort()[-10:][::-1]
l = np.vstack([h,a])
l = np.reshape(l, 20)
print "Top 10 hubs:"
print h
print "Top 10 authorities:"
print a
lh=np.array(h).tolist()
la=np.array(a).tolist()
lrh=np.array(854311*rh).tolist()
lra=np.array(5554311*ra).tolist()


import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
G.add_weighted_edges_from(arr)


A = G.subgraph(l)
pos=nx.shell_layout(A)


nx.draw_networkx_nodes(A,pos,
                       nodelist=np.array(h).tolist(),				#same plot as before
                       node_color='blue',					#hubs, blue
                       node_size=lrh,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=np.array(a).tolist(),
                       node_color='green',					#authorities, green
                       node_size=lra,
                   alpha=0.8)
nx.draw_networkx_edges(A, pos, width=1, alpha=0.3, edge_color='blue')
nx.draw_networkx_labels(A, pos, font_size=12, font_family='sans-serif')
plt.show()


