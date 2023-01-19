lst = [('Beginning iOS Programming', 534, 34.99),
       ('Beginning Android Programming', 484, 29.99),
       ('Python Machine Learning', 284, 39.99)]

# 1 - a
# lst.sort(key=lambda x: x[0])
# print(lst)

# 1 - b
# lst.sort(key=lambda x: x[1])
# print(lst)

# 1 - c
lst.sort(key=lambda x: x[2])
print(lst)

