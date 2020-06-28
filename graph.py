import numpy as np

class Graph:

    class Node:

        def __init__(self, n, x, y, albumN):
            self.edges = np.zeros(n,dtype=Graph.Node)
            self.x = x
            self.y = y
            self.album = np.zeros(albumN)
            self.bag = []

    def __init__(self, n, max_x, max_y, albumN):
        self.n = n
        self.max_x = max_x
        self.max_y = max_y
        self.albumN = albumN
        self.nodes = np.zeros(n,dtype=Graph.Node)

        #Creating all nodes

        for i in range(self.n):
            x = np.random.uniform(-max_x,max_x);
            y = np.random.uniform(-max_y,max_y);
            self.nodes[i] = Graph.Node(n=self.n,x=x, y=y, albumN=self.albumN)

        #Getting the average
        self.distances = np.zeros((n,n))
        avg = 0
        for i in range(0,n):
            for j in range(i,n):
                if(i == j): continue
                a = (self.nodes[i].x-self.nodes[j].x)
                b = (self.nodes[i].y-self.nodes[j].y)
                d = np.sqrt(a*a + b*b)
                #print("distance between[",i,",",j,"]","=",d)
                avg += d
                self.distances[i,j] = d
        avg /= (self.n*(self.n-1))

        #print("Average:", avg)

        #Making friends
        #dist = random.exponential(scale=avg, size=(self.n, self.n))
        for i in range(0,n):
            for j in range(i,n):
                if(i == j): continue
                rn = np.random.uniform(0,1);
                #print("Checking:","[",i,",",j,"]","for", rn ,"<=", avg/(avg + self.distances[i][j]) ," is ",rn <= avg/(avg + self.distances[i][j]))
                if(rn <= avg/(avg + self.distances[i][j])):
                    self.nodes[i].edges[j] = self.nodes[j]
                    self.nodes[j].edges[i] = self.nodes[i]
            #print("Node:",self.nodes[i],"\nEdges:\n",self.nodes[i].edges,"\n")
