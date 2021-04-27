# list 操作

def reverse(elems):
    i, j = 0, len(elems) - 1
    while i < j:
        elems[i], elems[j] = elems[j], elems[i]
        i, j = i+1, j-1


# 链表
class LNode:
    def __int__(self, elem, next_=None):
        self.elem = elem
        self.next = next_