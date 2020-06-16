import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.UID, root, root.step))

    def run(self, target):
        """ YOUR CODE HERE """
        distance = 9999
        target_found = 0
        while self.queue.empty() == 0:
            self.counter += 1
            q = self.queue.get()
            neighbor_list = self.graph.reveal_neighbors(q[1])
            if q[0] == target.UID:
                if distance > q[2]:
                    distance = q[2]
                    target_found = 1
            else:
                for neighbor in neighbor_list:
                    if neighbor.UID not in self.visited.keys():
                        self.visited.update({q[0]: q[1]})
                        if neighbor.step < distance:
                            self.queue.put((neighbor.UID, neighbor, neighbor.step))

        if target_found:
            return True, self.counter, distance
        else:
        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
            return False, 0, 0
