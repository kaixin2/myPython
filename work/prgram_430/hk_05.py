import pandas as pd


df = pd.read_csv("Automobile_data.csv")
# print(df)
# # 5 - a
# head_data = df.head(5)
# print(head_data)
#
# tail_data = df.tail(7)
# print(tail_data)

# # 5 - b
# max_price = df['price'].max()
# data = df[df['price'] == max_price]
#
# temp = data[['company','price']]
# print(temp)

# # 5 - c
# data = df.groupby('company')[['price']].max()
# print(data)

# 5 - d
# data = df.groupby('company')[['average-mileage']].mean()
# print(data)

# # 5 - e
# data = df.drop_duplicates(subset=['company'])
# companys = data.company.values
# for s in companys:
#     print(s)
#     le = len(s)
#     for i in range(0, le):
#         print('-', end='')
#     print()
#     temp = df[df['company'] == s]
#     temp = temp[['body-style', 'price']].sort_values(['price', 'body-style'], ascending=False)
#
#     for index in temp['body-style'].index:
#         t = temp['body-style'].get(index)
#         t2 = temp['price'].get(index)
#         print(t + " ", end='')
#         print(t2)

# 5 - f


def ask(*param):
    df = pd.read_csv("Automobile_data.csv")
    #
    # print(df.head(1))
    le = len(param)
    #
    # print(le)
    # print(param[0])
    # print(param[1])

    if le == 2:
        return df[(df['company'] == param[0]) & (df['wheel-base'] == param[1])]
    else:
        return df[(df['company'] == param[0]) & (df['wheel-base'] == param[1])
                  & (df['num-of-cylinders'] == param[2]) & (df['horsepower'] == param[3])]


print("请输入company:")
s = input();
print("请输入wheel-base:")
num1 = float(input())

print("请输入num-of-cylinders:")
s1 = input()
if s1 == "exit":
    res = ask(s, num1)
    print(res)
else:
    print("请输入horsepower:")
    num2 = float(input())
    res = ask(s, num1, s1, num2)
    print(res)

# alfa-romero
# 88.6
# four
# 111
#
