#
#   Fill in your personal details
#
#   NIU1: 1390690  Name: Eduard  Surname: Campo Raurich
#   NIU2: 1391716  Name: Roger   Surname: Prats Llivina
#

class Graph:
    def __init__(self,adjacent=[]):
        """
        Creates a Graph.
            :param adjacent: a list of tuples where the first element is a string 
        with a node name and the second a list of strings with all its neighbors.
        """
        self.adj=dict(adjacent)



    def getNodes(self):
        """
        Provides a list of strings with all the graph nodes.
        :return : A python array with all list nodes in ascending order
        """
        nodes=self.adj.keys()
        nodes.sort()
        return nodes

    def createFromBoolMatrix(self,mat):
       
        def pos2name(y,x):
            """
            Auxiliary functions that return a unique node name for every point in the map
            :return :string
            """
            return 'p_'+str(x)+'_'+str(y)
        self.adj={}
        numRow = len(mat)
        if (numRow >0):
            numCol = len(mat[0])
            for c in range(numCol):
                for f in range(numRow):
                    if mat[f][c] == True:
                        veins = []
                        if (f > 0 and mat[f-1][c] == True): #mirem a d'alt
                            veins.append(pos2name(f-1,c))
                        if (c < numCol-1 and mat[f][c+1] == True): #mirem a la dreta
                            veins.append(pos2name(f,c+1))
                        if (f < numRow-1 and mat[f+1][c] == True): #mirem a baix
                            veins.append(pos2name(f+1,c))
                        if (c > 0 and mat[f][c-1] == True): #mirem a l'esquerra
                            veins.append(pos2name(f,c-1))
                        self.adj[pos2name(f,c)] = veins           

    def loadFromBoolMatrix(self,fname):
        """
        Loads a boolean matrix from a text file and uses it to populate the graph
            :param fname: the path to an existing text file containing a boolean matrix.
        """
        mat=[[col=='T' for col in line.strip()] for line in open(fname).read().split('\n') if len(line.strip())]
        self.createFromBoolMatrix(mat)


    def getBFS(self,p1Label,p2Label):
        """
        Finds the shortest path bvetween two nodes if it exists.
        :param p1Label: a string with the node name to start the path
            :param p2Label: a string with the node name of the end of the path
        :return : A tuple with the legth (number of vertices) of shortest as an 
            integer and the shortest path as a python array of strings. 
            If there exists no path, (-1,[]) is returned.
        """
        graph = self.adj
        # if not graph.has_key(p1Label):
        #     return (-1,[])
        # if not graph.has_key(p2Label):
        #     return (-1,[])
        if (p1Label == p2Label):
            return (0,[p1Label])
        Level = {p1Label: 0}
        Parent = {p1Label: None}
        path = [p1Label]
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

    def isConnected(self):
        """
        Checks connectivity of the Graph.
        :return : True if the Graph is connected False otherwise
        """
        nodes = self.adj.keys()
        if len(nodes) > 0: #default answer for empty map -> True, because thats the answer in joc de proves
            inici = nodes[0]#choose a default node to check connectivity
            for i in self.adj:
                if (i != inici): #we don't need to check same node
                    try:
                        cami = self.getBFS(inici,i)
                        if (cami == (-1,[])):
                            return False
                    except:
                        return False
        return True

    def __repr__(self):
        """
        :return : A string containing a python expression that can build the graph.
        """
        adjList=self.adj.items()
        for a in adjList:
            a[1].sort()
        adjList.sort()
        return 'Graph('+str(adjList)+')'

    def __eq__(self, other):
        """
        :return : True if two graphs are exactly the same.
        """
        return repr(self)==repr(other)
