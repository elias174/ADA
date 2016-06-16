from collections import defaultdict
import collections


class Node(object):

    def __init__(self, data, color=None, d=0, pi=None, f=0):
        self.data = data
        self.color = color
        self.d = d
        self.f = f
        self.pi = pi


class MyGraph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        #properties = {'color':node1.color, 'd':node1.d, 'pi':node1.pi}
        self._graph[node1.data].add(node2)
        if not self._directed:
            self._graph[node2.data].add(node1.data)

    def remove(self, node):
        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

nodes = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F}
connections = [(A, B), (B, C), (B, D), (C, D), (E, F), (F, C)]

g = MyGraph(connections, True)

infi = 999999999999999


def bfs(G, s, nodes):
    for key, value in nodes.iteritems():
        node = nodes[key]
        node.color = 'WHITE'
        node.d = infi
        node.pi = ''
    s.color = 'GRAY'
    s.d = 0
    s.pi = None
    Q = collections.deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u.data]:
            if v.color == 'WHITE':
                v.color = 'GRAY'
                v.d = u.d + 1
                v.pi = u
                Q.append(v)
        u.color = 'BLACK'


def dfs(G):
    for key, value in nodes.iteritems():
        node = nodes[key]
        node.color = 'WHITE'
        node.pi = ''
    time = 0
    for key, value in nodes.iteritems():
        node = nodes[key]
        if node.color == 'WHITE':
            dfs_visit(G, node)


def dfs_visit(G, u):
    time = time + 1
    u.d = time
    u.color = 'GRAY'
    for v in G[u.data]:
        if v.color == 'WHITE':
            v.pi = u
            dfs_visit(G, v)
    u.color = 'BLACK'
    time = time + 1
    u.f = time

bfs(g._graph, d, nodes)
for v in g._graph[u.data]:
    print v.color, v.d
dfs(g._graph)
for v in g._graph[u.data]:
    print v.color, v.d, v.f