#!/usr/bin/env python3

import sys

class Graph(object):
  def __init__(self, v):
    self.adj = {}
    self.V = V
    for v in range(V):
      self.adj[v] = list()

  def addEdge(self, v, w):
    self.adj[v].append(w)
    self.adj[w].append(v)

class DFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    self.visited = [False for _ in range(g.V)]
    self.parent = [False for _ in range(g.V)]
    self.dfs(s)

  def dfs(self, v):
    self.visited[v] = True
    for w in self.g.adj[v]:
      if not self.visited[w]:
        self.parent[w] = v
        self.dfs(w)

  def hasPathTo(self, v):
    return self.visited[v]

  def PathTo(self, v):
    if not self.hasPathTo(v):
      return None
    path = [v]
    while v != self.s:
      v = self.parent[v]
      path.append(v)
    return path[::-1]


V = int(sys.stdin.readline())

g = Graph(V)

for line in sys.stdin:
  v, w = [int(t) for t in line.strip().split()]
  g.addEdge(v, w)

d = {}
for i in range(0, V):
  paths = DFSPaths(g, i)
  d['{}'.format(paths.visited)] = 1

print(len(d))
