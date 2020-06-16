import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        self.queue.put((self.manhattan_distance(self.root, target), self.root))
        self.visited.update({self.root.UID: self.root})
        while not self.queue.empty():
            self.counter += 1
            q_item = self.queue.get()
            if q_item[1].UID == target.UID:
                return True, self.counter, q_item[1].step
            else:
                neighbor_list = self.graph.reveal_neighbors(q_item[1])
                for neighbor in neighbor_list:
                    if neighbor.UID not in self.visited.keys():
                        self.visited.update({neighbor.UID: neighbor})
                        self.queue.put((q_item[1].step + self.manhattan_distance(neighbor, target)+1, neighbor))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
