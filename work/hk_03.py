#
# def cal_palindrome(s):
#     s1 = s
#     s2 = s
#     len_s = len(s)
#     if len_s == 1:
#         print("回文字1: ",s)
#         return
#
#     # 输出回文1
#     print("回文字1: ", end="")
#     print(s, end="")
#     for i in range(0, len_s):
#         print(s[len_s - 1 - i], end="")
#
#     print("\n回文字2: ", end="")
#     print(s, end="")
#     for i in range(0,len_s - 1):
#         print(s[len_s - 2 - i], end="")
#
#
# s = input()
# cal_palindrome(s)


# def cal_even():
#     ans = 0
#
#     for i in range(101, 201):
#         if i % 2 == 0:
#             ans += i
#     return ans
#
#
# print(cal_even())

# def cal():
#     mmax = 0
#     mmin = 100
#     av = 0
#
#     li = [2, 5, 6, 7, 8, 9, 2, 9, 9];
#     for i in li:
#         if i > mmax:
#             mmax = i
#         if i < mmin:
#             mmin = i
#         av += i
#     print("平均数:", av / len(li))
#     print("最大值:", mmax)
#     print("最小值:", mmin)
#
#
# cal()


def cal():

    li = ["flower", "flow", "flight"]
    min_len = 100
    for i in li:
        if len(i) < min_len:
            min_len = len(i)

    for i in range(0, min_len):
        if li[1][i] == li[0][i] and li[1][i] == li[2][i]:
            print(li[0][i], end="")
        else:
            break


cal()