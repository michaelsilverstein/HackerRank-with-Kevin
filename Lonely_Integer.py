def lonelyinteger(a):
    counts = [a.count(x) for x in a]
    unique_counts = []
    for i in counts:
        c = 0
        for j in counts:
            if i!=j:
                c += 1
        unique_counts.append(c)
    answer = a[unique_counts.index(max(unique_counts))]
