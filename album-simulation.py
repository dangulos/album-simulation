import numpy as np
from graph import Graph

def getAPrint(distrubutions):
    r = np.random.uniform(0,1)
    for i in range(0,distrubutions.shape[0]):
        if(r < distrubutions[i]):return i+1
        r = r - distrubutions[i]
    return -1

def simulation(n,max_x, max_y, albumN):
    g = Graph(n=n, max_x=max_x, max_y=max_y, albumN=albumN)
    dist = np.random.uniform(0,1,albumN)
    distributions = np.zeros(albumN)
    total = np.sum(dist)
    for i in range(0,albumN):
        distributions[i] = dist[i]/total
    print(distributions)
    while(False):
        for i in range(0,g.nodes.shape[0]):
            p = getAPrint(distributions)
            if(g.nodes[i].album[p-1]==0):
                g.nodes[i].album[p-1]
            else:
                g.nodes[i].bag.push(p)
        for i in range(0,g.nodes.shape[0]):
            for j in range(0,g.nodes[i].edges.shape[0]):
                if(g.nodes[i].edges[j] == 0):continue
                for k in range(0,g.nodes[i].album):
                    if(g.nodes[i].album[k] == 1): continue





if __name__ == "__main__":
    simulation(n=100,max_x=100, max_y=100, albumN=6)