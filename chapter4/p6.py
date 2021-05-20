# 二叉树
class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, x):
        self._elems.append(x)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()


def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)

def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.pop().right
        else:
            t = None


class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def self_root(self, rootnode):
        self._root = rootnode

    def self_left(self, leftchild):
        self._root.left = leftchild

    def self_right(self, rightchild):
        self._root.right = rightchild


if __name__ == "__main__":
    tree = BinTNode(1, BinTNode(3, BinTNode(5, BinTNode(0)), BinTNode(4, None, BinTNode(7))),
                    BinTNode(8, None, BinTNode(9, BinTNode(6))))
    preorder(tree, lambda x: print(x, end=" "))
    preorder_nonrec(tree, lambda x: print(x, end=" "))