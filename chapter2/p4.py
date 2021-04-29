from Python_data_structure.chapter2.p3 import LCList
import time

class josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while self._rear is not None:
            self.turn(m-1)
            print(self.pop(), end="\n" if self.is_empty() else ",")


def josephus_l(n, k, m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=("," if num > 1 else "\n"))

    return
t1 = time.time()
josephus(10, 2, 7)
t2 = time.time()
josephus_l(10, 2, 7)
t3 = time.time()
print(t2-t1)
print(t3-t2)