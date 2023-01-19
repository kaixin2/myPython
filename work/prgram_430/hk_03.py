import numpy as np

a1 = np.round(20 * np.random.random((4, 5)), 2)

# 3 - a
print(a1)

# 3- b
for i in a1:
    tot = 0
    for j in i:
        tot += j
    print(tot / len(i))
# 3 - c

min_avg = 100
for i in a1:
    tot = 0
    for j in i:
        tot += j
    min_avg = min(min_avg,tot / len(i))

res = 100
min_dis = 100
for i in a1:
    for j in i:
        if np.abs(j - min_avg) < min_dis:
            res = j
            min_dis = np.abs(j - min_avg)
print(res)


