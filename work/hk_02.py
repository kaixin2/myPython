import random
end = 14
a = random.randint(1, end)
b = random.randint(1, end)
c = random.randint(1, end)
d = random.randint(1, end)
li = [a, b, c, d]
print("使用的4个数为: ", li)
op = ["+", "-", "*", "/"]
flag = [0, 0, 0, 0]


def cal(step, num):
    result = 0

    try:
        if step == 4:
            first = num[0]
            second = num[1]
            third = num[2]
            fourth = num[3]
            for op1 in op:
                for op2 in op:
                    for op3 in op:
                        # 因为* / + - 的优先级不同,如果分类讨论很麻烦,所以用括号将每一次运算都括起来,这样就只剩下一种运算顺序,就是从内括号往外括号计算,这样只需要枚举符号和数的位置就可以
                        # 用正则格式化计算表达式
                        express = "((first{0}second){1}third){2}fourth".format(op1, op2, op3)
                        # eval函数可以对表达式进行求值
                        if eval(express) == 24:
                            print("(({0}{1}{2}){3}{4}){5}{6} ".format(first, op1, second, op2, third, op3, fourth))
                            result = 1
    # 抛异常
    except ZeroDivisionError:
        return result

    t = num
    for i in range(0, 4):
        if flag[i] == 1:
            continue
        else:
            flag[i] = 1
            t.append(li[i])
            result = result | cal(step + 1, t)
            t.pop()
            flag[i] = 0

    return result


res = cal(0, [])
if res == 1:
    print("You Win!")
else:
    print("You Lose!")





