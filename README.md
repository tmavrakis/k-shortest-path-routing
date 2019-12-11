# k-shortest-path-routing
Implementation of k shortest path routing using Python

I implement the k algorithm for finding the shortest paths in python using the basic Dijkstra algorithm.
The network topology will be variable and defined at the beginning of my program, with
a array-like presentation. The column-rows in the table will define both the link and the
cost of it. For example the element a ij = 5 will specify that the cost from node i to j
is 5. All links will be bidirectional at the same cost (ie aij = aji = 5).
The program at its output prints: (a) the typology used and (b)
k paths calculated per pair of nodes.

The user can gives he's own topology or choose to use the default topology.
The default topology shown below.


