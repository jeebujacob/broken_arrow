import sys,os
from graph_tool.all import *

#############################  Reading graph from file   ###########################################



from array import *


ug = Graph(directed=False)
fh=open('branches.txt','r')
d=fh.readlines()

lenfile = len(d)
linecount=0

array4vertex = []
countelement = 0
countvertex = 0
prev = 0
post = 0
ug.add_vertex(8)                                 ## The vertex are set to be 8 in number, but the user can decide which all are the nets



for i in d:                                                                              ## Reading each line
                                                                                           #print "the lines are",
      for k in i:                                                                         ## Reading each letter
                                                                                            #print kk
        if k != '\n' and k == ',':
          if d[linecount][countelement+1] != '\n':
            prev = int(d[linecount][countelement-1])
            post = int(d[linecount][countelement+1])
            
           
            if prev not in array4vertex:
                   
                  array4vertex.append(prev)
                  countvertex = countvertex + 1
                  
                 
            if post not in array4vertex:
                  array4vertex.append(post)
                   
                  countvertex = countvertex + 1
                     
            ug.add_edge(ug.vertex(prev), ug.vertex(post))                            ############ adding edges in graph ##########       
        
        countelement = countelement + 1
      countelement = 0
      linecount = linecount + 1
countelement = 0

print("\n")
print "vertices in graph"                                                            ########### printing vertices in graph #########

print array4vertex

print("\n")
print "branches in graph"                                                            ########### printing edges in graph #########

for e in ug.edges():
    print e



fh.close() 


################  adding property map to vertices and edges ##################

v_partition = ug.new_vertex_property("int")
e_weight = ug.new_edge_property("int")

##########################   initial partitioning ##############################
v_partition[ug.vertex(0)] = 1
v_partition[ug.vertex(1)] = 1
v_partition[ug.vertex(3)] = 1
v_partition[ug.vertex(4)] = 1                 ####  assigned two different partitions
v_partition[ug.vertex(2)] = 2
v_partition[ug.vertex(5)] = 2
v_partition[ug.vertex(6)] = 2
v_partition[ug.vertex(7)] = 2
#################################  creating two lists ##########################
partition1 = []
vlist1 = []
vlist1.append(0)
vlist1.append(1)
vlist1.append(3)
vlist1.append(4)
partition1.append(vlist1)
partition2 = []
vlist2 = []
vlist2.append(2)
vlist2.append(5)
vlist2.append(6)
vlist2.append(7)
partition2.append(vlist2)
#################################  added edges  ##################################

############################   specified wieghts to edges  ################################
for e in ug.edges():
  e_weight[e]=1

eg = ug.edge(4,6)
ce = ug.edge(2,4)
df = ug.edge(3,5)

e_weight[eg]=2
e_weight[ce]=2
e_weight[df]=2

print "\n"
print "weights of edges"
for e in ug.edges():
   print e
   print "weight = " ,                                                                     ########### printing weights of edges in graph #########
   print e_weight[e]
   print "\n"

#############################################################################################
print("\n")

graph_draw(ug,vertex_text=ug.vertex_index,vertex_font_size=18,output_size=(200,200),output="./kl_graph.pdf")
######################## initializations  ########################################
G = 0
index = 0
Ex = Ix = 0
cx = 0
n1 = 0
n2 = 0
m1 = 0
m2 = 0
Gfinal = -5
cutsize = [5,0,0,0,0]
vlist3 = [1,1,1,1]
vlist4 = [2,2,2,2]
vlist5 = [1,1,1,1]
vlist6 = [2,2,2,2]
vlist7 = [1,1,1,1]
vlist8 = [2,2,2,2]
vlist9 = [1,1,1,1]
vlist10= [2,2,2,2]
vlist11= [1,1,1,1]
vlist12= [2,2,2,2]
partition1.append(vlist3)
partition2.append(vlist4)
partition1.append(vlist5)
partition2.append(vlist6)
partition1.append(vlist7)
partition2.append(vlist8)
partition1.append(vlist9)
partition2.append(vlist10)
partition1.append(vlist11)
partition2.append(vlist12)

vswap1 = 0
vswap2 = 0
#################### printing unpartitioned graph #####################
print"\n**********Before partition",

print"*****************"

 
 
print"\n"
print "partition I" 
for v in partition1[0]:

    v2 = ug.vertex(v)  
    print v2


print"\n"
print "partition II" 
for v in partition2[0]:
   
    v2 = ug.vertex(v)  
    print v2
print"\n"
print "cutsize = "
print 5
########################### Gain calculations ###############################
for i in [0,1,2,3]:

  for v19 in partition1[i]:
          
           v1 = ug.vertex(v19)
           if v_partition[v1] != 3:
             for w in v1.out_neighbours():
     
                if v_partition[w]==1:
                    s = ug.edge(v1,w)
                    Ix += e_weight[s]
                                                      ### for each node in first partition which is not swapped ##### 
                if v_partition[w]==3:
                    s = ug.edge(v1,w)
                    Ix += e_weight[s]


         
                if v_partition[w]==2:
                     s = ug.edge(v1,w)
                     Ex +=  e_weight[s]
               
                if v_partition[w]==4:
                     s = ug.edge(v1,w)
                     Ex +=  e_weight[s]
  
                
            
             d1 = Ex - Ix
             Ex = Ix = 0

             Ey = Iy = 0
           
             for v20 in partition2[i]:
                    
                  v2 = ug.vertex(v20)
                  if v_partition[v2] != 4:
                    for x in v2.out_neighbours():
     
                        if v_partition[x]==2:
                           s = ug.edge(v2,x)
                           Iy += e_weight[s]
                       
                        if v_partition[x]==4:
                           s = ug.edge(v2,x)
                           Iy += e_weight[s]

                                                      ### for each node in second partition which is not swapped ##### 

  
                        if v_partition[x]==1:
                            s = ug.edge(v2,x)
                            Ey +=  e_weight[s]
                 
                        if v_partition[x]==3:
                            s = ug.edge(v2,x)
                            Ey +=  e_weight[s]
 
                        if x == v1:
                           s = ug.edge(v1,v2)
                           cx = e_weight[s]
                    
                         
                    d2 = Ey - Iy
                    Ey = Iy = 0                      ########### gain calculations for nodes found above ##################
                    G = d1+d2
                    G -= 2*cx
                     
                    if G > Gfinal:
                       Gfinal = G
                       m1 = n1
                       m2 = n2                                 ################ finding elements to be swapped ####################      
                       vswap1 = v19
                       vswap2 = v20
                    G = 0
                    cx =0 
   
                    n2+=1
                  if v_partition[v2] == 4 :
                    
                    n2+=1
             n2 = 0
             n1+=1
           if v_partition[v1] == 3:
            
             n1+=1
  n1 = 0
  cutsize[i+1] = cutsize[i] - Gfinal
  Gfinal = -5
  


  for j in [0,1,2,3]:
     
     partition1[i+1][j]=partition1[i][j]  
     partition2[i+1][j]=partition2[i][j]                  
 
  partition1[i+1][m1]=vswap2  
  partition2[i+1][m2]=vswap1                                   ################### swapping elements ##############################    
  v11 = ug.vertex(vswap1)
  v21 = ug.vertex(vswap2)
  v_partition[v11]=4  
  v_partition[v21]=3                                          ################### marking swapped elements ##########################
  print"\n**********After step no",
  print i+1,
  print"*****************"

  print"\n"
  print "swapped vertices"
  print  vswap1
  print  vswap2
 
  print"\n"
  print "partition I" 
  for v in partition1[i+1]:

    v2 = ug.vertex(v)  
    print v2
                                                          ###########  printing each state output #############################

  print"\n"
  print "partition II" 
  for v in partition2[i+1]:
   
    v2 = ug.vertex(v)  
    print v2

  print"\n"
  print "cutsize = "
  print cutsize[i+1]
min_cutsize = min(cutsize) 
index = cutsize.index(min_cutsize)
######################## printing final output #############################
print"\n**********Final Step",
print"*****************"

print"\n"
print "partition I" 
for v in partition1[index+1]:

    v2 = ug.vertex(v)  
    print v2


print"\n"
print "partition II" 
for v in partition2[index+1]:
   
    v2 = ug.vertex(v)  
    print v2


###################### Printing final cutsize ################################
print "cutsize array"
print cutsize
