from Graph import *

edge = [[False, True, False, False, False, False, False, False], [False, True, True, True, True, False, True, False], [False, False, True, False, True, False, True, False], [False, False, False, False, True, False, True, True], [False, True, True, True, True, False, True, False], [False, True, False, False, False, False, True, False], [False, True, True, True, True, True, True, False], [False, False, False, False, False, True, True, False]]

circle = [[True, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [True, False, True, True, True, True, True, True, True, True, True, True, True, True, False], [True, True, True, False, False, True, True, False, False, False, False, False, False, True, False], [False, False, False, False, False, False, True, True, False, False, False, False, True, True, False], [False, False, False, False, False, False, False, True, True, False, False, False, True, False, False], [False, False, False, False, False, False, False, False, True, True, False, False, True, True, False], [False, True, True, True, False, False, False, False, False, True, True, False, False, True, False], [False, False, True, False, False, False, False, False, False, False, True, True, False, True, False], [False, True, True, True, False, False, False, False, False, False, False, True, True, True, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]

noedge =[[False, False, False, False, False, False, False, False], [False, True, True, True, True, False, True, False], [False, False, True, False, True, False, True, False], [False, False, False, False, True, False, True, False], [False, True, True, True, True, False, True, False], [False, True, False, False, False, False, True, False], [False, True, True, True, True, True, True, False], [False, False, False, False, False, False, False, False]]

mapa = [[False, False, False, False, False, False, False, False, False, False, False, False], [False, True, True, False, False, False, True, False, False, True, True, False], [False, False, True, True, True, True, True, True, True, True, False, False], [False, True, True, False, False, False, True, False, False, True, True, False], [False, True, False, False, True, False, True, False, False, False, False, False], [False, True, False, True, True, True, False, True, True, True, True, False], [False, True, False, False, False, True, True, True, False, False, True, False], [False, True, True, True, False, False, True, False, False, True, True, False], [False, False, False, True, False, False, False, True, True, True, False, False], [False, False, False, True, True, True, False, True, False, True, False, False], [False, True, True, True, False, True, True, True, False, True, True, False], [False, False, False, False, False, False, False, False, False, False, False, False]]

def graf(mat):
	def pos2name(y,x):
	    """
	    Auxiliary functions that return a unique node name for every point in the map
	    :return :string
	    """
	    return 'p_'+str(x)+'_'+str(y)
	numRow = len(mat)
	numCol = len(mat[0])
	adj = {}
	if (numRow >0):
		for c in range(numCol):
		    for f in range(numRow):
		    	if mat[f][c] == True:
			        veins = []
			        if (f < numRow-1 and mat[f+1][c] == True): #mirem a baix
			            veins.append(pos2name(f+1,c))
			        if (c > 0 and mat[f][c-1] == True): #mirem a l'esquerra
			            veins.append(pos2name(f,c-1))
			        if (f > 0 and mat[f-1][c] == True): #mirem a d'alt
			            veins.append(pos2name(f-1,c))
			        if (c < numCol-1 and mat[f][c+1] == True): #mirem a la dreta
			            veins.append(pos2name(f,c+1))
			        
			        
			        adj[pos2name(f,c)] = veins		       
	return adj
	          





def minim(adj, p1Label, p2Label):
	graph = adj
	if not graph.has_key(p1Label):
		return (-1,[])
	if not graph.has_key(p2Label):
		return (-1,[])
	if (p1Label == p2Label):
		return (0,[p1Label])
	Level = {p1Label: 0}
	Parent = {p1Label: None}
	path = [p1Label]
	visitats={}
	i = 1
	while path:
	    next = []
	    for u in path:
	        for v in graph[u]:
	        	
				if (v not in Level):
					Level[v] = i
					Parent[v] = u
					next.append(v)
	    path = next
	    i+=1
	aux = p2Label
	minim = [p2Label]
	try:
		for p in range(Level[p2Label]):
		    aux = Parent[aux]
		    minim.append(aux)
	except:
		return (-1,[])
	return (len(minim)-1, list(reversed(minim)))

circl = graf(circle)
edg = graf(edge) 
noedg = graf(noedge)
mapaa = graf(mapa)    


def is_connected(graph):
        nodes = graph.keys()
        inici = nodes[0]
        for i in graph:
        	cami = minim(graph,inici,i)
        	if cami == (-1,[]):
        		return False
        return True
print is_connected(circl)
print is_connected(edg)
print is_connected(noedg)

print "circle F, edge T ,noedge T, empty T" 

 					