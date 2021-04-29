import time
import random

def get_next(p_s):
    i, k, m = 0, -1, len(p_s)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p_s[i] == p_s[k]:
            i += 1
            k += 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def get_next_my(p_s):
    m = len(p_s)
    if m == 0:
        return []
    pmt = [0] * m
    count = 0
    for i in range(1, m):
        if p_s[i] == p_s[count]:
            pmt[i] = count + 1
            count += 1
        else:
            pmt[i] = 0
            count = 0
    pnext = pmt[0:-1]
    pnext.insert(0, -1)
    return pnext

## KMP
def KMP(t_s, p_s):
    n, m = len(t_s), len(p_s)
    pnext = get_next_my(p_s)
    count = 0
    for i in range(1, m):
        if p_s[i] == p_s[count]:
            pnext[i] = count + 1
            count += 1
        else:
            count =0

    i, j = 0, 0

    while i < n and j < m:
        if j == -1 or t_s[i] == p_s[j]:
            j += 1
            i += 1
        else:
            j = pnext[j]

    if j == m:
        return i - j
    return -1

#
# ll = ''
# for i in range(10000):
#     #lint = random.randint(97, 123)
#     lint = random.randint(97, 105)
#     ll += chr(lint)
#
# print(ll)
# p_s = ll
# t1 = time.time()
# pnext = get_next_my(p_s)
# t2 = time.time()
# pnext2 = get_next(p_s)
# t3 = time.time()
# print(t2-t1)
# print(pnext)
# print(t3-t2)
# print(pnext2)

t_s = "abccdafbafafffaawd"
p_s = "bafaf"
index = KMP(t_s, p_s)
if index != -1:
    print(t_s[index:index+len(p_s)])
    print(p_s)