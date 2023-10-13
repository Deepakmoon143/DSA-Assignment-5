class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []


def count_nodes(root, level):
    if not root:
        return 0

    queue = [(root, 0)]
    count = 0

    while queue:
        node, current_level = queue.pop(0)

        if current_level == level:
            count += 1
        elif current_level > level:
            break

        for i in node.children:
            queue.append((i, current_level + 1))

    return count


def build_tree():
    node_dict = {}
    root_value = int(input("Enter the value of the root node: "))
    root = Tree(root_value)
    node_dict[root_value] = root

    queue = [root]

    while queue:
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.value}: "))

        for i in range(num_children):
            child_value = int(input(f"Enter the value of child {i+1} for node {current_node.value}: "))
            child = Tree(child_value)
            current_node.children.append(child)
            node_dict[child_value] = child
            queue.append(child)

    return root

root_node = build_tree()
level = int(input("Enter the level to count nodes: "))

count = count_nodes(root_node, level)
print(f"Number of nodes at level {level}: {count}")
