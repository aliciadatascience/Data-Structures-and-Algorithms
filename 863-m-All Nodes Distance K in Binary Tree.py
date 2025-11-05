https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# time complexity:o(N)
# space complexity:o(N)


class Solution:
    def distanceK(self, root, target, K):
        import collections
        def build_graph(node, parent):
            if not node:
                return

            if parent:
                self.graph[node].append(parent)
            if node.left:
                self.graph[node].append(node.left)
                build_graph(node.left, node)
            if node.right:
                self.graph[node].append(node.right)
                build_graph(node.right, node)

        # self.graph is a hashmap
        self.graph = collections.defaultdict(list)
        build_graph(root, None)
        seen = set()
        result = []
        queue = collections.deque()
        queue.append([target, 0])

        while queue:
            node, level = queue.popleft()

            if node in seen:
                continue
            seen.add(node)

            if level == K:
                result.append(node.val)
            else:
                for connected in self.graph[node]:
                    queue.append([connected, level + 1])
        return result








