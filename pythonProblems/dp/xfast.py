import functools

prime_const = 7


class Node:
    def __init__(self, value) -> None:
        self.value = bin(value)[2:]


def hashing_function_1(value, arrsize):
    # product of the sum of the integer values of the value passed in
    return (sum([int(x) for x in value]) * prime_const) % arrsize


def hashing_function_2(value, arrsize):
    # sum of the products of each number in value
    return (functools.reduce(lambda x, y: x + y, functools.reduce(lambda x: x * prime_const, [int(x) for x in value]))) % arrsize


class LevelHash:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = {}
        return self

    def new_level(self, level):
        self.nodes[level] = [-1] * 4
        self.num_nodes[level] = 0
        return self

    def hash_value(self, value, level):
        hashed_value = hashing_function_1(value, len(self.nodes))
        if self.nodes[level][hashed_value] != -1:
            ## occupied, cuckoo hashing
            hashed_value = hashing_function_2(value, len(self.nodes))
            # place in second value
            self.nodes[level][hashed_value] = Node(value)
        else:
            ## is empty
            self.nodes[level][hashed_value] = Node(value)

    def rehash(self, level):
        node_values: list[Node] = [x for x in self.nodes[level]]
        self.nodes[level] = [-1] * (len(self.nodes[level]) * 2)
        self.num_nodes[level] = 0
        for each_node_value in node_values:
            self.hash_value(each_node_value.value, level)
            self.num_nodes[level] += 1
        ## all values hashed, return self
        return self

    def insert_node_at_level(self, node: Node, level: int):
        if level not in self.nodes:
            ## level does not exist
            self = self.new_level(level)
        else:
            if self.num_nodes[level] / len(self.nodes[level]) >= .70:
                ## double size, aka rehash
                self.rehash(level)
            self.hash_value(node.value, level)
            self.num_nodes[level] += 1


class XFastTree:

    def __init__(self):
        self.root = None
