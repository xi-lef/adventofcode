import networkx as nx

risks = {}
for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        risks[x + 1j * y] = int(c)
end = x + 1j * y

graph = nx.DiGraph()
for pos in risks:
    for d in (1, -1, 1j, -1j):
        npos = pos + d
        if npos in risks:
            graph.add_edge(pos, npos, w = risks[npos])
print(nx.shortest_path_length(graph, 0, end, 'w'))

w = end.real + 1
h = end.imag + 1
for pos, risk in risks.copy().items():
    for tx in range(5):
        for ty in range(5):
            x, y = pos.real, pos.imag
            nrisk = (risk + tx + ty)
            risks[tx * w + x + 1j * (ty * h + y)] = (nrisk - 1) % 9 + 1

graph = nx.DiGraph()
for pos in risks:
    for d in (1, -1, 1j, -1j):
        npos = pos + d
        if npos in risks:
            graph.add_edge(pos, npos, w = risks[npos])
print(nx.shortest_path_length(graph, 0, 5 * (w + 1j * h) - 1 - 1j, 'w'))
