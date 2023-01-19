# networkX_E4.py
# Demo of minimum spanning tree(MST) with NetworkX
# Copyright 2021 YouCans, XUPT
# Crated：2021-05-21

import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
import networkx as nx  # 导入 NetworkX 工具包

G = nx.Graph()  # 创建：空的 无向图
G.add_weighted_edges_from([(1, 2, 50), (1, 3, 60), (2, 4, 65), (2, 5, 40), (3, 4, 52),
                           (3, 7, 45), (4, 5, 50), (4, 6, 30), (4, 7, 42),
                           (5, 6, 70)])  # 向图中添加多条赋权边: (node1,node2,weight)

T = nx.minimum_spanning_tree(G)  # 返回包括最小生成树的图




pos=nx.spring_layout(G);
nx.draw(G, pos, with_labels=True, alpha=0.8)  # 绘制无向图
labels = nx.get_edge_attributes(G, 'weight')  # YouCans, XUPT
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='c')  # 显示边的权值
nx.draw_networkx_edges(G, pos, edgelist=T.edges, edge_color='r', width=4)  # 设置指定边的颜色

plt.show()
