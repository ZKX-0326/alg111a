import random
import math

# 城市的数量
num_cities = 10

# 城市坐标
cities = []
for i in range(num_cities):
  cities.append((random.randint(-100, 100), random.randint(-100, 100)))

# 计算两个城市之间的距离
def distance(city1, city2):
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# 随机搜索算法
best_distance = float("inf")
for i in range(10000):
  # 随机排列城市
  permutation = random.sample(cities, num_cities)
  distance = 0
  # 计算路径总长度
  for i in range(num_cities):
    distance += distance(permutation[i], permutation[(i + 1) % num_cities])
  # 如果当前路径更短，则更新最优解
  if distance < best_distance:
    best_distance = distance
    best_permutation = permutation

# 输出最优解
print(best_distance)
print(best_permutation)