import math
import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
import networkx as nx  # 导入 NetworkX 工具包

class Temp:
    id = 0
    li = []


class Node:
    u = 0
    v = 0
    dis = 0

    def toString(self):
        return self.u + " " + self.v


filename = "C:\\Users\\21592\\Desktop\\mouse_embryo_data.csv"
f = open(filename, "r")
line = f.readline()
cnt = 0
data = []
while line:
    line = line.replace("\n", "")
    arr = []
    if cnt != 0:
        arr = list(map(float, line.split(",")))
        d = Temp()
        d.id = cnt
        d.li = arr
        data.append(d)

    cnt += 1
    line = f.readline()
f.close()


def getDis(t1:[], t2: []):
    dis = 0
    for i in range(len(t1)):
        dis += (t1[i] - t2[i]) * (t1[i] - t2[i])
    return math.sqrt(dis)


nodes = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        node = Node()
        node.u = data[i].id
        node.v = data[j].id
        node.dis = getDis(data[i].li, data[j].li)
        nodes.append(node)


edge=[]
for e in nodes:
    t=(e.u,e.v,e.dis)
    edge.append(t)



G = nx.Graph()  # 创建：空的 无向图
G.add_weighted_edges_from(edge)
T = nx.minimum_spanning_tree(G)  # 返回包括最小生成树的图


nx.draw(T,nx.spring_layout(T),with_labels=True, alpha=0.8);

# pos=nx.spring_layout(G);
# nx.draw(G, pos, with_labels=True, alpha=0.8)  # 绘制无向图
# labels = nx.get_edge_attributes(G, 'weight')  # YouCans, XUPT
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='c')  # 显示边的权值
# nx.draw_networkx_edges(G, pos, edgelist=T.edges, edge_color='r', width=4)  # 设置指定边的颜色

plt.show()
