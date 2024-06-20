# 參考 https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-%E5%84%AA%E5%8C%96%E7%AE%97%E6%B3%95/01-%E5%82%B3%E7%B5%B1%E5%84%AA%E5%8C%96%E6%96%B9%E6%B3%95/01-%E5%84%AA%E5%8C%96/01-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95/03-%E9%80%9A%E7%94%A8%E7%9A%84%E7%88%AC%E5%B1%B1%E6%A1%86%E6%9E%B6/tsp.py
import random

# 定義城市座標
citys = [
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

# 計算兩點之間的距離
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 計算整個路徑的總距離
def path_length(path):
    dist = 0
    plen = len(path)
    for i in range(plen):
        dist += distance(citys[path[i]], citys[path[(i + 1) % plen]])
    return dist

def hill_climbing(citys):
    path = list(range(len(citys)))
    length = path_length(path)
    
    # 嘗試交換路徑中的每一對城市
    for i in range(len(path) - 1):
        for j in range(i + 1, len(path)):
            new_path = path[:]
            new_path[i], new_path[j] = new_path[j], new_path[i]
            new_length = path_length(new_path)
                
            # 計算新路徑的長度
            if new_length < length:
                path, length = new_path, new_length
                print(f'Improved path: {path}, improved path_length: {length}')
                    
    return path, length

# 執行爬山演算法並打印最佳路徑和距離
best_path, best_length = hill_climbing(citys)
print("\r")
print(f'best path: {best_path}')
print(f'best path_length: {best_length}')