from collections import defaultdict

graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
adj_list = defaultdict(list)
print(adj_list)
for u, v in graph:
  adj_list[u].append(v)

print(adj_list.get('A'))