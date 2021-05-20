class SubtreeIndexError(ValueError):
    pass


def Tree(data, *subtrees):
    tree = [data]
    tree.extend(subtrees)
    return tree

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i + 1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree

def set(ss, *sub):

    return [ss].extend(sub)


class TreeNode:
    def __init__(self, data, subs=[]):
        self._data = data
        self._subtrees = list(subs)

    def __str__(self):
        return "[TreeNode {0} {1}]".format(self._data, self.subtrees)

if __name__ == "__main__":
    tree1 = Tree('+', 1, 2, 3)
    tree2 = Tree('*', tree1, 6, 8)
    print(tree1)
    print(tree2)
    set_subtree(tree1, 2, Tree("+", 3, 5))
    print(tree1)

