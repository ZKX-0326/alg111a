# 獨立頂點集問題
## 題目解析
給一張圖G=(V,E)，V為圖中所有頂點的集合，E為圖中所有邊的集合，找出一個子集合S，並使S中任兩點間沒有邊相鄰。
此問題也被應用在計算機網路設定、線性規劃以及機器學習。

以下為ChatGPT以貪婪法解決此問題的程式碼，我已完全理解其原理。

貪婪法為一種在當前狀況下選則最優解的方法。

## 由ChatGPT產生的結果(僅修改註解)
```
def independent_set(G):
  # 初始化獨立頂點集
  S = set()
  # 按照點的度数由大到小進行排序
  sorted_nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
  # 遍歷每個點
  for u in sorted_nodes:
    # 如果u的鄰居都不在S中，將u加入S
    if all(v not in S for v in G[u]):
      S.add(u)
  # 返回獨立頂點集
  return S

# 創建一張圖
G = nx.Graph()

# 向圖中添加邊
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

# 調用獨立點集函數求解
solution = independent_set(G)

# 輸出解决方案
print(solution)
```
我讓他用貪婪法解此問題，並已完全理解。

參考資料:   
[ChatGPT](https://openai.com/blog/chatgpt/)   
[維基百科](https://zh.wikipedia.org/zh-tw/%E7%8B%AC%E7%AB%8B%E9%9B%86)