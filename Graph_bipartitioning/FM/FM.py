# Author: Arun C (10307938)Aniruddha Shelke(11307R013),Jeebu Jacob Thomas(Roll no: 11307R010), 
# Description: Fiduccia Mattheyses Algo Implementation 
# Date: 01-12-2012
# Institution: IIT Bombay
# Vertices Count is limited to 8 (cannot change the count) but one can change the nets(upto 16 nets can be created) in the graph from nets.txt
# Space Constraint is (3,5) elements in partition 0 and partition 1 respectively
# Please refer the documentation of the code attached along


from graph_tool.all import *
from array import *


gr = Graph(directed=False)
fh=open('nets.txt','r') ## Opeing the file
cc=fh.readlines() ## Reading lines from the file

lenfile = len(cc)
linecount=0

array4vertex = []
countelement = 0
countvertex = 0
prev = 0 
post = 0
## The vertex are set to be 8 in number, but the user can decide which all are the nets
## This is because the demonstration is using (3,5) area constraint, so there is not point in having flexibility  for addition of vertices
a = gr.add_vertex()
b = gr.add_vertex()
c = gr.add_vertex()
d = gr.add_vertex()
e = gr.add_vertex()
f = gr.add_vertex()
g = gr.add_vertex()
h = gr.add_vertex()
## Defining a maximum of 16 nets allowed though a total of 8C2 nets are possible
netone = []
nettwo = []
netthree = []
netfour = []
netfive = []
netsix = []
netseven = []
neteight = []
netnine = []
netten = []
neteleven = []
nettwelve = []
netthirteen = []
netfourteen = []
netfifteen = []
netsixteen = []

for ii in cc: ## Reading each line 
      #print "the lines are",ii
      for kk in ii: ## Reading each letter
	    #print kk
	    if kk != '\n' and kk == ',':
		  if cc[linecount][countelement+1] != '\n':
			prev = int(cc[linecount][countelement-1])
			post = int(cc[linecount][countelement+1])
			#print "prev = ",prev,"post = ",post
			
			if prev not in array4vertex:
			      array4vertex.append(prev)
			      countvertex = countvertex + 1
			      
			if post not in array4vertex:
			      array4vertex.append(post)
			      countvertex = countvertex + 1	
			gr.add_edge(gr.vertex(prev), gr.vertex(post))      
	     
	    countelement = countelement + 1
      countelement = 0
      linecount = linecount + 1
countelement = 0

##### Net Description #######################################


for netstage in range (1,lenfile+1):
	for netelem in cc[netstage-1]:
        	if netelem != '\n' and netelem != ' ' and netelem != ',':
			if netstage == 1:
				netone.append(int(netelem)) 
			elif netstage == 2:
				nettwo.append(int(netelem))
			elif netstage == 3:
				netthree.append(int(netelem))
			elif netstage == 4:
				netfour.append(int(netelem))
			elif netstage == 5:
				netfive.append(int(netelem))
			elif netstage == 6:
				netsix.append(int(netelem))
			elif netstage == 7:
				netseven.append(int(netelem))
			elif netstage == 8:
				neteight.append(int(netelem))
			elif netstage == 9:
				netnine.append(int(netelem))
			elif netstage == 10:
				netten.append(int(netelem))
			elif netstage == 11:
				neteleven.append(int(netelem))
			elif netstage == 12:
				nettwelve.append(int(netelem))
			elif netstage == 13:
				netthirteen.append(int(netelem))
			elif netstage == 14:
				netfourteen.append(int(netelem))
			elif netstage == 15:
				netfifteen.append(int(netelem))
			elif netstage == 16:
				netsixteen.append(int(netelem))

      
fh.close() 



print "netone" ,netone
print "nettwo" ,nettwo


vlock = gr.new_vertex_property("int")
vgain = gr.new_vertex_property("int")
vnets = gr.new_vertex_property("vector<int>")
vpart = gr.new_vertex_property("int")   



#Defining the initial partitioning of the vertices

vpart[gr.vertex(0)] = 0
vpart[gr.vertex(2)] = 0
vpart[gr.vertex(3)] = 0
vpart[gr.vertex(6)] = 0
vpart[gr.vertex(1)] = 1
vpart[gr.vertex(4)] = 1
vpart[gr.vertex(7)] = 1
vpart[gr.vertex(5)] = 1

########################################################################################################

######Initial Cut Size assigned as 6#########################################
cutsize = 6
#############################################################################	



#Defining the Graph Initial Properties
len_vert = 0
len_edge = 0


vgain[gr.vertex(gr.vertex_index[a])] = 0
vgain[gr.vertex(gr.vertex_index[c])] = 0
vgain[gr.vertex(gr.vertex_index[d])] = 0
vgain[gr.vertex(gr.vertex_index[g])] = 0
vgain[gr.vertex(gr.vertex_index[b])] = 0
vgain[gr.vertex(gr.vertex_index[e])] = 0
vgain[gr.vertex(gr.vertex_index[h])] = 0
vgain[gr.vertex(gr.vertex_index[f])] = 0



partition_array = [[0 for x in xrange(20)] for x in xrange(20)] 
gain_array = [[0 for x in xrange(20)] for x in xrange(20)] 
gain_array2 = [0,0,0,0,0,0,0,0]
gainsigma = [0,0,0,0,0,0,0,0]
cutsize_array = [0,0,0,0,0,0,0,0]


count = 0
count2 = 0
count3 = 0
FS = 0
TE = 0
#####################################Drawing the Graph #################################################

graph_draw(gr,vertex_text=gr.vertex_index,vertex_font_size=18,output_size=(200,200),output="./FM.pdf")



for i in gr.vertices():
	
	vlock[gr.vertex(i)] = 0
	vgain[gr.vertex(i)] = 0

#################### ALGORITHM STARTS HERE ######################################################################################
gain = array('i',[0,0,0,0,0,0,0,0])


for n in gr.vertices():  # Number of times to change the partitions of the vertices is the number of vertices in the graph itself!!!!
	
	print "Stage",n,"Results :"
	for vertices in gr.vertices(): # For finding the gain of each vertex
	      if vlock[gr.vertex(vertices)] == 0 :
	      
	
	      ###################### GAIN Calculation #########################################################
	     
		    if int(vertices) in netone:
			  #print "yes",vertices,"is present in netone"
			  
			  for j in netone:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1
					    
			  #print "count =",count
			  #print "count2 =",count2
			  #print "len of netone = ",len(netone)
			  if count == len(netone) - 1:
				FS = FS+1
			  if count2 == len(netone) - 1:  
				TE = TE+1
			  count = 0
			  count2 = 0
			  
	      #############################################################################################
		    if int(vertices) in nettwo:
			  #print "yes",i,"is present in nettwo"
			  for j in nettwo:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count =",count
			  #print "count2 =",count2
			  #print "len of nettwo = ",len(nettwo)
			  if count == len(nettwo) - 1:
				FS = FS+1
			  if count2 == len(nettwo) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      #############################################################################################
		    if int(vertices) in netthree:
			  #print "yes",i,"is present in netthree"
			  for j in netthree:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netthree = ",len(netthree)
			  if count == len(netthree) - 1:
				FS = FS+1
			  if count2 == len(netthree) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################

		    if int(vertices) in netfour:
			  #print "yes",i,"is present in netfour"
			  for j in netfour:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netfour=",len(netfour)
			  if count == len(netfour) - 1:
				FS = FS+1
			  if count2 == len(netfour) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################

		    if int(vertices) in netfive:
			  #print "yes",i,"is present in netfive"
			  for j in netfive:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netfive",len(netfive)
			  if count == len(netfive) - 1:
				FS = FS+1
			  if count2 == len(netfive) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################

		    if int(vertices) in netsix:
			  #print "yes",i,"is present in netsix"
			  for j in netsix:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netsix=",len(netsix)
			  if count == len(netsix) - 1:
				FS = FS+1
			  if count2 == len(netsix) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################
	      

		    if int(vertices) in netseven:
			  #print "yes",i,"is present in netseven"
			  for j in netseven:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netseven=",len(netseven)
			  if count == len(netseven) - 1:
				FS = FS+1
			  if count2 == len(netseven) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      
	      
		    if int(vertices) in neteight:
			  #print "yes",i,"is present in neteight"
			  for j in neteight:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of neteight=",len(neteight)
			  if count == len(neteight) - 1:
				FS = FS+1
			  if count2 == len(neteight) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	      
	      
		    if int(vertices) in netnine:
			  #print "yes",i,"is present in netnine"
			  for j in netnine:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netnine=",len(netnine)
			  if count == len(netnine) - 1:
				FS = FS+1
			  if count2 == len(netnine) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	  
	      
	      
		    if int(vertices) in netten:
			  #print "yes",i,"is present in netten"
			  for j in netten:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netten=",len(netten)
			  if count == len(netten) - 1:
				FS = FS+1
			  if count2 == len(netten) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	  
	      
		    if int(vertices) in neteleven:
			  #print "yes",i,"is present in netteleven"
			  for j in netteleven:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netteleven=",len(netteleven)
			  if count == len(netteleven) - 1:
				FS = FS+1
			  if count2 == len(netteleven) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	 
	      
		    if int(vertices) in nettwelve:
			  #print "yes",i,"is present in nettwelve"
			  for j in nettwelve:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of nettwelve=",len(nettwelve)
			  if count == len(nettwelve) - 1:
				FS = FS+1
			  if count2 == len(nettwelve) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      		      
	      
	      
		    if int(vertices) in netthirteen:
			  #print "yes",i,"is present in netthirteen"
			  for j in netthirteen:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netthirteen=",len(netthirteen)
			  if count == len(netthirteen) - 1:
				FS = FS+1
			  if count2 == len(netthirteen) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	  
	      
		    if int(vertices) in netfourteen:
			  #print "yes",i,"is present in netfourteen"
			  for j in netfourteen:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netfourteen=",len(netfourteen)
			  if count == len(netfourteen) - 1:
				FS = FS+1
			  if count2 == len(netfourteen) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################	      	 
	      
		    if int(vertices) in netfifteen:
			  #print "yes",i,"is present in netfifteen"
			  for j in netfifteen:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netfifteen=",len(netfifteen)
			  if count == len(netfifteen) - 1:
				FS = FS+1
			  if count2 == len(netfifteen) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################		      
	      
		    if int(vertices) in netsixteen:
			  #print "yes",i,"is present in netsixteen"
			  for j in netsixteen:
				if int(j) != int(vertices):	
				      if vpart[gr.vertex(int(j))] != vpart[gr.vertex(int(vertices))]:
					    count = count+1
				      elif vpart[gr.vertex(int(j))] == vpart[gr.vertex(int(vertices))]: 
					    count2 = count2 + 1      
			  #print "count = ",count
			  #print "count2 =",count2
			  #print "len of netsixteen=",len(netsixteen)
			  if count == len(netsixteen) - 1:
				FS = FS+1
			  if count2 == len(netsixteen) - 1:  
				TE = TE+1
			  count = 0
			  count2= 0
	      ##############################################################################################		      	      
	      
	      
	      
		    GAIN = FS - TE
		    vgain[gr.vertex(vertices)] = GAIN
		    print "FS of ",vertices,"=",FS
		    print "TE of ",vertices,"=",TE
		    print "GAIN of",vertices,"=",GAIN
		    FS = 0
		    TE = 0
	    
		###############################################################################################################
		    
		    gain[int(vertices)] = vgain[gr.vertex(vertices)]	 ## Array to store the gain values in the respective alphabetical indice of the vertex
		    
		    gain_array[int(n)][int(vertices)]=vgain[gr.vertex(vertices)]
			  
					  
	      else:    
		    vgain[gr.vertex(vertices)] = -50 ## Some minimum value given to the already locked Vertices so as not to interfere in the next gain calculation
		    gain[int(vertices)] = vgain[gr.vertex(vertices)]
		    
	      partition_array[int(n)][int(vertices)]=vpart[gr.vertex(vertices)]     
		    
		
	#To find out which vertice has the highest gain 
	
	
	print "Original Gain is:"
	for z in gain:
	      print z
	
	gain_mirror = sorted(gain,reverse=True) # Sort in the Descending Order
	print "Descending Gain is:"
	for z in gain_mirror:
	      print z
	
	#Calculate Partition0 and Partition1 Counts of vertices
	
	part0count = 0
	part1count = 0
	for pcounts in gr.vertices():
		
		if 0 == vpart[gr.vertex(pcounts)]  :
			part0count = part0count + 1
		elif 1 == vpart[gr.vertex(pcounts)] :
			part1count = part1count + 1
			
	
	for pp in gr.vertices():
		aa = gain.index(gain_mirror[int(pp)])   #Finding the index of the highest gain vertex
		print "swapping vertex is :",aa
		#Using a Case-Similar If Construct for finding whether the vertex follows Area constraint (3,5)		    
		if vlock[gr.vertex(aa)] == 0 :
			      
		      if  vpart[gr.vertex(aa)] == 0 :                         ##If in 0th partition
			    if  (2 < part0count-1 < 6) and (2 < part1count+1 < 6):   ## Whether it satisfies the area constraint ?
				  vlock[gr.vertex(aa)] =  1  			     ## The vertex is locked
				  vpart[gr.vertex(aa)] =  1                          ## Partition of the vertex is swapped
				  print "swap element is:",int(aa)
				  print "Gain of the swap element is:",vgain[gr.vertex(aa)]
				  #print "pp value is:",int(pp)
				  gain_array2[count3] =  vgain[gr.vertex(aa)]
				  count3 = count3 + 1
				  break		  
		      elif vpart[gr.vertex(aa)] == 1 :                  ##If in 1st partition
			    if  (2 < part1count-1 < 6) and (2 < part0count+1 < 6):   ## Whether it satisfies the area constraint ?
				  vlock[gr.vertex(aa)] = 1     		      ## The vertex is locked
				  vpart[gr.vertex(aa)] = 0                          ## Partition of the vertex is swapped
				  print "swap element is:",int(aa)
				  print "Gain of the swap element is:",vgain[gr.vertex(aa)]
				  gain_array2[count3] =  vgain[gr.vertex(aa)]
				  count3 = count3 + 1
				  break 
		     ## vgain[gr.vertex(int(aa))] = -51 	 
		      gain[aa] = -51 ##### Just a default value to take care when 2 or more indices have same gain values 
		      print"vertice:",int(aa),"didnt satisfy area constraint"    
		
		      
#print" Gain array "		      

#for kk in gr.vertices():
      #print gain_array2[int(kk)],

#print " " 
print "######################"
print " Partition Table " 
print "######################"
for i in gr.vertices():
      for j in gr.vertices():
	    print partition_array[int(i)][int(j)], 
      print " "      
	
	
###############################Finding the best partition###############################################
print "######################"
print " Final Cutsize " 
print "######################"
for i in gr.vertices():	
      if i == 0:
	    gainsigma[int(i)] = gain_array2[int(i)] 
	    
      else:
	    k = int(i) - 1
	    gainsigma[int(i)] =  gainsigma[k] + gain_array2[int(i)]
      
      cutsize_array[int(i)] = cutsize - gainsigma[int(i)]
      print cutsize_array[int(i)]
     
index_final = min(cutsize_array)  
final = cutsize_array.index(index_final)	    
print "index_final is",final

print "######################"
print "Final Partition is :"
print "######################"
for s in gr.vertices(): 
      if int(s) == 0:
	    print "a = ",partition_array[final+1][int(s)] 
      elif int(s) == 1:
	    print "b = ",partition_array[final+1][int(s)] 
      elif int(s) == 2:
	    print "c = ",partition_array[final+1][int(s)] 
      elif int(s) == 3:
	    print "d = ",partition_array[final+1][int(s)] 
      elif int(s) == 4:
	    print "e = ",partition_array[final+1][int(s)] 
      elif int(s) == 5:
	    print "f = ",partition_array[final+1][int(s)] 
      elif int(s) == 6:
	    print "g = ",partition_array[final+1][int(s)] 
      elif int(s) == 7:
	    print "h = ",partition_array[final+1][int(s)] 
    
print " "      
print "######################" 
 

print "Hooray its done!!" 




##################################Testing Zone######################################################################################

  
