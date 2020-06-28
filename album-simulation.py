import numpy as np
from graph import Graph

class Observer:
    def __init__(self):
        self.completedAlbums = 0
        self.totalPrints = 0
        self.printsInAlbums = 0
        self.freePrints = 0
        self.totalDays = 0

def getAPrint(distrubutions):
    r = np.random.uniform(0,1)
    for i in range(0,distrubutions.shape[0]):
        if(r < distrubutions[i]):return i+1
        r = r - distrubutions[i]
    return -1

def simulation(n,max_x, max_y, albumN):
    g = Graph(n=n, max_x=max_x, max_y=max_y, albumN=albumN)
    o = Observer()
    dist = np.random.uniform(0,1,albumN)
    distributions = np.zeros(albumN)
    total = np.sum(dist)
    for i in range(0,albumN):
        distributions[i] = dist[i]/total
    print(distributions)
    while(o.printsInAlbums != n*albumN):
        o.totalDays = o.totalDays + 1
        print(o.totalDays)
        for i in range(0,g.nodes.shape[0]):
            p = getAPrint(distributions)
            o.totalPrints = o.totalPrints + 1
            if(g.nodes[i].album[p-1]==0):
                g.nodes[i].album[p-1] = 1
                o.printsInAlbums = o.printsInAlbums + 1
            else:
                g.nodes[i].bag.append(p)
                o.freePrints = o.freePrints + 1
        for i in range(0,g.nodes.shape[0]):
            for j in range(0,g.nodes[i].edges.shape[0]):
                if(g.nodes[i].edges[j] == 0):continue
                for k in range(0,g.nodes[i].album.shape[0]):
                    if(g.nodes[i].album[k] == 1): continue
                    if(k+1 in g.nodes[i].edges[j].bag):
                        g.nodes[i].edges[j].bag.remove(k+1)
                        g.nodes[i].album[k] = 1
                        o.freePrints = o.freePrints - 1
                        o.printsInAlbums = o.printsInAlbums + 1

if __name__ == "__main__":
    simulation(n=100,max_x=1000, max_y=1000, albumN=6)