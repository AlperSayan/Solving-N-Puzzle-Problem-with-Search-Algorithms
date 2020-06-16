class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        while self.stack:
            tmp_node = self.stack.pop()
            neighbor_list = self.graph.reveal_neighbors(tmp_node)
            self.counter += 1
            if target.UID == tmp_node.UID:
                return True, self.counter, tmp_node.step
            else:
                if tmp_node.UID in self.visited.keys():
                    continue
                self.visited.update({tmp_node.UID: tmp_node})
                for neighbor in neighbor_list:
                    self.stack.append(neighbor)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
