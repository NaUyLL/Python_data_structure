def josephus_l(n, k, m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=("," if num > 1 else "\n"))

    return

josephus_l(10, 2, 7)
