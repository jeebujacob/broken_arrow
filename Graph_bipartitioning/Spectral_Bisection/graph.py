##Author : Arun C, Jeebu Jacob Thomas, Aniruddha Shelke 
##Description : A loose implementation of Spectral Bisection Graph Bipartitioning
#Date: 01-12-12
#Institution: IIT Bombay


from numpy.linalg import *
from numpy import matrix
from graph_tool.all import *
#import graph_tool 
g = load_graph("simple.xml")
graph_draw(g,vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200, 200),
           output="graph.pdf")
m1 = graph_tool.spectral.laplacian(g,normalized=False,sparse=False)
#m1=([2,-1,0,0,-1,0],[-1,3,-1,0,-1,0],[0,-1,2,-1,0,0],[0,0,-1,3,-1,-1],[-1,-1,0,-1,3,0],[0,0,0,-1,0,1])--wikipedia algebraic connectivity
#m1=([3,-1,-1,-1],[-1,2,-1,0],[-1,-1,3,-1],[-1,0,-1,2])
#m1=([1,-1,0,0,0,0,0],[-1,2,-1,0,0,0,0],[0,-1,3,-1,0,-1,0],[0,0,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,-1,0,-1,3,-1],[0,0,0,0,0,-1,1])
print " The Laplacian matrix is given by:"

print (m1)
w,v=linalg.eig(m1)
print " Eigen Values are ",w
print "\n"

print " Eigen vectors in the same order are "
print(v)
print "\n\n\n"
s=sorted(w)
print "Select the Eigen Vector corresponding to ",s[1],"which will give the partition index of each vertex  depending on wheter the element is positive or negative" 
#l=graph_tool.centrality.eigenvector(g) 
#print(l)

