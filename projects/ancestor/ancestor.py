#ancestors - list of (parent, child) relationships
#vertex - integer identifier for parent or child
#each child can be a parent and each parent can be a child

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    # child-parents pairs
    parent_dict = {}
    end_nodes = set()
    for item in ancestors:
        if not parent_dict.get(item[-1]):
            parent_dict[item[-1]] = set([item[0]])
        else:
            parent_dict[item[-1]].add(item[0])
    def recursive_helper(node, dict):
        nonlocal end_nodes

        print(f"At node {node}")

        if dict.get(node) is None:
            print(f"No parents for node {node}")
            end_nodes.add(node)

        else:
            for node in dict.get(node):
                recursive_helper(node, dict)

    recursive_helper(starting_node, parent_dict)
    print(f"Parents dictionary: {parent_dict}")

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))
