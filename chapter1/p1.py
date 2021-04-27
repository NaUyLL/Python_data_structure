import networkx as nx
import matplotlib.pyplot as plt
import time


class my_Graph():
    def __init__(self, martix, node_name=None):
        self.martix = martix
        if point_name:
            self.node_name = node_name
        self.nodes = [i for i in range(len(martix))]
        self.edges = []
        self._get_edges()


    def _get_edges(self):
        self.edges = []
        for i in range(len(self.nodes)):
            for j in range(i, len(self.nodes)):
                if matrix[i][j] == 1:
                    self.edges.append((i, j))



# 牛顿迭代法求平方根:
def new_sqrt(x, err = 1e-6):
    y = 1.0
    while abs(y**2 - x) > err:
        y = (y + x/y) / 2
    return y

# 贪心算法，红绿灯
point_name = ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'DA', 'DB', 'DC', 'EA', 'EB', 'EC', 'ED']
matrix = [
   # AB AC AD BA BC BD DA DB DC EA EB EC ED
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0], # AB
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0], # AC
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], # AD
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # BA
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], # BC
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0], # BD
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], # DA
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0], # DB
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # DC
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # EA
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], # EB
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], # EC
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # ED
]

def not_adjacent_with_set(v, group, G):
    if not group:
        return True
    for n_v in group:
        if G.martix[v][n_v] == 1:
            return False
    return True


def coloring(G):
    color = 0
    groups = []
    verts = G.nodes.copy()
    try:
        node_name = G.node_name
    except:
        node_name = verts
    while verts:
        new_group = []
        newverts = verts.copy()
        for v in newverts:
            if not_adjacent_with_set(v, new_group, G):
                new_group.append(v)
                verts.remove(v)
        groups.append((color, new_group))
        color += 1
    new_verts = G.nodes
    for _, group in groups:
        for v in new_verts:
            if v not in group:
                if not_adjacent_with_set(v, group, G):
                    group.append(v)

    name_groups = []
    for color, group in groups:
        name_group = []
        for i in group:
            name_group.append(node_name[i])
        name_groups.append((color, name_group))

    return name_groups


"""F0=F1=1 Fn=Fn-1+Fn-2"""
def fib1(n):
    if n < 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    a = b = 1
    for i in range(1, n):
        a, b = b, a + b
    return b

# 高斯消元法：
test_m = [
    [16.0, 17.0, 20.0, 8.0],
    [5.0, 72.0, 8.0, 10.0],
    [2.0, 7.0, 8.0, 19.0],
    [100.0, 50.0, 21.0, 35.0],
]
def Gaussian_Elimination(M):
    assert len(M) == len(M[0])
    n = len(M)
    lam_list = []
    for i in range(n-1):
        for j in range(i+1, n):
            lam = M[i][i] / M[j][i]
            lam_list.append(1/lam)
            for k in range(n):
                M[j][k] = lam * M[j][k] - M[i][k]

    det = 1
    for i in lam_list:
        det *= i
    for i in range(n):
        det *= M[i][i]

    print(M)
    return det





if __name__ == "__main__":
    # g = new_sqrt(0.09)
    # print(g)
    # print(g**2)
    # G = my_Graph(matrix, point_name)
    # print(coloring(G))
    # t1 = time.time()
    # #print(fib1(35))
    # t2 = time.time()
    # print(fib2(10000))
    # t3 = time.time()
    # print(t2-t1)
    # print(t3-t2)
    test_m2 = [[3,2],
               [4,-1]]
    print(Gaussian_Elimination(test_m2))

