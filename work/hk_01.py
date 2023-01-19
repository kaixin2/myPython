
def school(professional, score_line, need_stu_num, *tea_name, name="hku", **apply_stu_and_code):
    print("学校名称:", name)
    print("专业:", professional)
    print("招生分数:", score_line)
    print("招生人数:", need_stu_num)
    print("招生老师名单:", tea_name)
    print("报考考生名单及其分数:", apply_stu_and_code)

    d = apply_stu_and_code
    cnt = 0 # 计算达标人数
    li = []
    for stu in d:
        # print(stu + " ", end='')
        # print(d[stu])
        if d[stu] >= score_line:
            cnt = cnt + 1
            li.append(stu)

    r = len(li)
    # print(r)
    # 按分数高低排序
    for i in range(0,r):
        for j in range(i, r - 1):
            # print("i = ", i, "j = ", j)
            if d[li[j + 1]] > d[li[j]]:
                # print(d[li[j + 1]])
                # print(d[li[j]])
                temp = li[j + 1]
                li[j + 1] = li[j]
                li[j] = temp
    print(li)
    print("达限人数:", cnt)
    print("录取名单:")
    for i in li:
        print("姓名:", i, "成绩:", d[i])

    print("录取人数", min(cnt, need_stu_num))


# 杨幂=分数,后面可以继续添加这样的参数
# 中间的名字也可以添加
school('软件工程', 550, 37, '周润发', '周星驰', '周文', '徐良', 杨幂=570, 贾玲=580, 沈腾=555)