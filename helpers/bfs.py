# Untitled.py
# Created by Kids on 3/6/21.

graph_ht = {'A' : ['B', 'C'], 'B' : ['D', 'E'], 'C' : ['F'], 'D' : [], 'E' : ['F'], 'F' : []}
def bfs(start, end):
	considered = []
	queue = [[start]]
	while len(queue) != 0:
		current_node = queue.pop(0)
 		considered.append(graph_ht[param1[1]])