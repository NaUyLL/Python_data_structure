# 哈夫曼树：
from p6 import BinTNode, preorder
from p4 import PrioQueue

class HTNode(BinTNode):
    def __lt__(self, other):
        return self.data < other.data


class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()


weights = [2,3,7,4,10,2,5]
q = HuffmanTree(weights)
preorder(q, lambda x: print(x, end=" "))