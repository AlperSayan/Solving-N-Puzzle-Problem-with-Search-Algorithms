class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue:
            tmp_node = self.queue.pop(0)
            self.counter += 1
            neighbor_list = self.graph.reveal_neighbors(tmp_node)
            if tmp_node.UID == target.UID:
                return True, self.counter, tmp_node.step
            else:
                for neighbor in neighbor_list:
                    if neighbor.UID not in self.visited.keys():
                        self.queue.append(neighbor)
                        self.visited.update({neighbor.UID: neighbor})

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
