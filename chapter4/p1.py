#  栈与队列

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


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in SStack.top()")
        return self._top.elem

    def push(self, x):
        self._top = LNode(x, self.top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in SStack.pop()")
        x = self._top.elem
        self._top = self._top.next
        return x

class ESStack(SStack):
    def depth(self):
        return len(self._elems)


def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())


def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2:
            raise SyntaxError("Short of operand(s).")
        a = st.pop()
        b = st.pop()
        if x == "+":
            c = b + a
        elif x == "-":
            c = b - a
        elif x == "*":
            c = b * a
        elif x == "/":
            c = b / a
        else:
            break

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")


def suffix_exp_calcuator():
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end": return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)


def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight>0 and n<1):
        return False
    if knap_rec(weight- wlist[n-1], wlist, n-1):
        print("Item " + str(n) + ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else: return False

if __name__ == "__main__":
    # st1 = SStack()
    # st1.push(3)
    # st1.push(7)
    # while not st1.is_empty():
    #     print(st1.pop())
    suffix_exp_calcuator()