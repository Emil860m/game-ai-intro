import heapq
import math
from nodes import Node, NodeGroup

def get_distance_between_nodes(node1, node2):
    x = node1.position.x - node2.position.x
    y = node1.position.y - node2.position.y
    return math.sqrt(x**2 + y**2)


        

class Pathfinding:
    def __init__(self, nodes):
        self.nodes = nodes
        self.seen_nodes = []
    
    def add_node_to_queue(self, node, previous, queue):
        if not node in queue:
            node.priority = previous.priority + get_distance_between_nodes(previous, node)
            node.previous = previous
            heapq.heappush(queue, node)
        else:
            nodeq = queue[queue.index(node)]
            if nodeq.priority > previous.priority + get_distance_between_nodes(previous, node):
                return
            queue.remove(nodeq)
            node.priority = previous.priority + get_distance_between_nodes(previous, node)
            node.previous = previous
            heapq.heappush(queue, node)

    def dijkstra(self, start_node, target):
        # set up queue and current = startnode
        #[(priority, value)]
        self.seen_nodes = []
        target = self.nodes.getNodeFromPixels(target.x, target.y)
        queue = []
        start_node = self.nodes.getNodeFromPixels(start_node.x, start_node.y)
        node = start_node
        if target is None or node is None:
            return []
        node.priority = 0
        for i in node.neighbors:
            if node.neighbors[i] is not None and not node.neighbors[i] in self.seen_nodes:
                self.add_node_to_queue(node.neighbors[i], node, queue)
        self.seen_nodes.append(node)
        node = heapq.heappop(queue)
        # if we have not arrived, check neighbours
        while (not node == target) and len(queue) > 0:
            for i in node.neighbors:
                if node.neighbors[i] is not None and not node.neighbors[i] in self.seen_nodes:
                    self.add_node_to_queue(node.neighbors[i], node, queue)
            self.seen_nodes.append(node)
            node = heapq.heappop(queue)
            
        
        route = []
        if node == target:
            while node.previous != start_node:
                route.append(node)
                node = node.previous
        self.route = route
        if len(route) > 1:
            for i in route:
                print(i)
        return route




