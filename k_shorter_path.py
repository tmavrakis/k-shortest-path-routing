import os
import sys
from collections import defaultdict

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.paths = []
        self.costs = []
        self.prev = []
        for i in range(vertices): self.prev.append([])
        self.dist = []
        for i in range(vertices): self.dist.append([])

    def clear(self):
        self.prev.clear()
        for i in range(self.V): self.prev.append([])
        self.dist.clear()
        for i in range(self.V): self.dist.append([])
        self.paths.clear()
        self.costs.clear()

    def addEdge(self, s, t, w):
        #undiractional
        self.graph[s].append([t, w])
    
    def printTopology(self):
        find = False
        for i in range(self.V):
            for j in range(self.V):
                if i == j: 
                    print("0", end=" ")
                else:
                    for t, w in self.graph[i]:
                        if t == j:
                            print(w, end=" ")
                            find = True
                            break
                    if find == True: find = False
                    else: print("0", end=" ")
            print("\n")

    def printPaths(self):
        temp = 0
        for i in self.paths:
            i.reverse()
            print(i)
            print("With correspoding cost: ", end="")
            print(self.costs[temp])
            temp = temp + 1

    def findmin(self, target):
        node = 0 #index of min node
        layer = 0
        min = sys.maxsize
        for i in range(self.V):
            count = 0 #index of layer with min dist
            for j in self.dist[i]:
                if j[0] <= min and j[1] == False:
                        min = j[0]
                        node = i
                        layer = count
                count = count + 1
      

        if node == target:
            self.dist[target][layer][1] = True
            self.paths.append([])
            self.updatePaths(target, layer, self.paths[-1])
            self.costs.append(self.dist[node][layer][0])
           
            ######remove duplicate###########

            seen = {-1}
            for x in self.paths[-1]:
                if x not in seen: seen.add(x)
                else:
                    self.paths.pop()
                    self.costs.pop()
                    break

            #find again min, and not target node
            node, layer = self.findmin(target)
        
        return node, layer
    
    def updatePaths(self, target, layer, path):
        path.append(target)
        if self.prev[target][layer] != -1:
            self.updatePaths(self.prev[target][layer][0], self.prev[target][layer][1], path)
    

    def DijkstraAllPaths(self, source, target, times):
        #initialization

        self.dist[source].append([0, False])
        self.prev[source].append(-1)
        node = 0
        layer = 0

        while len(self.paths) < times :

            keepup = False
            for i in range(self.V):
                for j in self.dist[i]:
                    if j[1] == False: keepup = True
            
            if keepup == False: 
                print("Not available paths exist for:")
                break


            node, layer = self.findmin(target)
            u = node
            
            self.dist[u][layer][1] = True #mark it
            for t, w in self.graph[u] : # t will be adjacency nodes, w will be cost of u - t
                
                self.dist[t].append([self.dist[u][layer][0] + w, False])
                self.prev[t].append((u,layer))



def makeTopology(g):
    choose = "garbage"
    valid = False
    while choose != "Exit" :
        try:
            choose = input("Give the two nodes and the cost you want to declare. Format 'node 1' 'node 2' 'cost between nodes'.\nOr type Exit to leave.\n").capitalize()
            if choose != "Exit":
                split = choose.split()
                node1 = int(split[0])
                node2 = int(split[1])
                cost = int(split[2])
            valid = True
        except:
            valid = False
            print("Valid number. Please give an integer.\n")
        else:
            if node1 >= g.V or node2 >= g.V:
                valid = False
                print("Node name should be lower than {}".format(g.V))
        
        if valid == True:
            g.addEdge(node1, node2, cost)


def defaultTopology(g):
    f = open(os.path.join(__location__, "defaultTopology.txt"))
    for x in f:
        split = x.split()
        g.addEdge(int(split[0]), int(split[1]), int(split[2]))
    f.close()

def main():
    while True:
        try:
            choose = int(input("Select action\n1)Give your topology\n2)Run the default topology\n"))
        except:
            print("Please give an integer.\n")
        else:
            if choose == 1 or choose == 2: break
            else: print("Give valid number.\n")
    
    if choose == 1:
        while True:
            try:
                numNodes = int(input("Select the total number of node in the graph.\n"))
                break
            except:
                print("Please give an integer.\n")
        g = Graph(numNodes)
        makeTopology(g)
    elif choose == 2: 
        g = Graph(14)
        defaultTopology(g)


    while True:
        try:
            k = int(input("Select k, the number shorters path.\n"))
            break
        except:
            print("Please give an integer.\n")

    print("Topology:")
    g.printTopology()
    for i in range(g.V):
        for j in range(i+1, g.V):
            g.DijkstraAllPaths(i, j, k) #finds paths

            print("Source: {}\nTarget: {}".format(i,j))
            g.printPaths() #print the paths and cost
            g.clear() #clear the path list to take the next one

main()
 
