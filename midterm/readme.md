# 旅行推銷員問題
## 題目解析
給一組城市和各城市之間的距離，求路過所有城市並回到起始城市的最短路徑。

## 由ChatGTP產生的結果
```
import random
import math

# 城市的數量
num_cities = 10

# 賦予各城市(x,y)座標
cities = []
for i in range(num_cities):
  cities.append((random.randint(-100, 100), random.randint(-100, 100)))

# 計算兩個城市之間的距離
def distance(city1, city2):
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# 隨機搜索演算法
best_distance = float("inf")
for i in range(10000):
  # 隨機排列城市
  permutation = random.sample(cities, num_cities)
  distance = 0
  # 計算路徑總長度
  for i in range(num_cities):
    distance += distance(permutation[i], permutation[(i + 1) % num_cities])
  # 如果當前路徑更短，則更新最優解
  if distance < best_distance:
    best_distance = distance
    best_permutation = permutation

# 輸出結果
print(best_distance)
print(best_permutation)
```

目前已完全理解此程式碼運行原理，此原理為將所有城市進行隨機排序並計算，再做比較進而得出結果。

參考資料:   
[ChatGTP](https://openai.com/blog/chatgpt/)   
[維基百科](https://zh.wikipedia.org/zh-tw/%E6%97%85%E8%A1%8C%E6%8E%A8%E9%94%80%E5%91%98%E9%97%AE%E9%A2%98)