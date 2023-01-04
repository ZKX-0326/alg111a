def independent_set(G):
  # 初始化独立点集为空
  S = set()
  # 按照点的度数从大到小排序
  sorted_nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
  # 遍历每个点
  for u in sorted_nodes:
    # 如果u的邻居都不在S中，则将u加入S
    if all(v not in S for v in G[u]):
      S.add(u)
  # 返回独立点集
  return S

# 创建一张图
G = nx.Graph()

# 向图中添加边
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

# 调用独立点集函数求解
solution = independent_set(G)

# 输出解决方案
print(solution)
