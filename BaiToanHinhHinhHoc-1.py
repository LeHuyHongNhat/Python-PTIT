import math
from itertools import combinations


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def are_collinear(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) == (p3[1] - p1[1]) * (p2[0] - p1[0])


def circumcenter(p1, p2, p3):
    if are_collinear(p1, p2, p3):
        return None
    d = 2 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    if d == 0:
        return None
    ux = ((p1[0] ** 2 + p1[1] ** 2) * (p2[1] - p3[1]) + (p2[0] ** 2 + p2[1] ** 2) * (p3[1] - p1[1]) +
          (p3[0] ** 2 + p3[1] ** 2) * (p1[1] - p2[1])) / d
    uy = ((p1[0] ** 2 + p1[1] ** 2) * (p3[0] - p2[0]) + (p2[0] ** 2 + p2[1] ** 2) * (p1[0] - p3[0]) +
          (p3[0] ** 2 + p3[1] ** 2) * (p2[0] - p1[0])) / d
    return ux, uy


def solve(points, K):
    points = list(set(points))  # Loại bỏ các điểm trùng lặp
    for p1, p2, p3 in combinations(points, 3):
        center = circumcenter(p1, p2, p3)
        if center is None:
            continue
        radius = distance(center, p1)
        radius_sq = radius ** 2  # Sử dụng bình phương bán kính để tránh tính toán căn bậc hai
        count = 0
        for p in points:
            if p not in (p1, p2, p3):  # Không tính các điểm nằm trên đường tròn
                if distance(center, p) ** 2 < radius_sq:  # So sánh bình phương khoảng cách
                    count += 1
        if count == K:
            return "YES"
    return "NO"


def main():
    try:
        T = int(input())
        for _ in range(T):
            N = int(input())
            K = int(input())
            points = [tuple(map(int, input().split())) for _ in range(N)]
            print(solve(points, K))
    except Exception as e:
        print("NO")


if __name__ == "__main__":
    main()
