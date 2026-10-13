from fractions import Fraction

def print_matrix(m):
    #첨가행렬 출력
    for row in m:
        left = " ".join(f"{str(v):>5}" for v in row[:-1])
        print(f"[{left} | {str(row[-1]):>5}]")
    print()

"""
연립방정식
  x1 - 2x2 +  x3 = 0
     2x2 - 8x3 = 8
-4x1 + 5x2 + 9x3 = -9
"""

m = [
    [1, -2, 1, 0],
    [0, 2, -8, 8],
    [-4, 5, 9, -9]
]

#분수를 정확히 계산하기 위한 변환
m = [[Fraction(v) for v in row] for row in m]

print("1. 초기 첨가행렬")
print_matrix(m)

#세 번째 행의 x1 계수를 0으로 만든다.
m[2] = [m[2][j] + 4 * m[0][j] for j in range(4)]

print("2. R3 <- R3 + 4R1")
print_matrix(m)

#두 번째 행의 피벗을 1로 만든다.
m[1] = [v / 2 for v in m[1]]

print("3. R2 <- R2 / 2")
print_matrix(m)

#세 번째 행의 x2 계수를 0으로 만든다.
m[2] = [m[2][j] + 3 * m[1][j] for j in range(4)]

print("4. R3 <- R3 + 3R2: 삼각형 형태 완성")
print_matrix(m)

#후진 대입: 마지막 방정식부터 역순으로 계산
n = 3
x = [Fraction(0) for _ in range(n)]

print("5. 후진 대입")
for i in range(n - 1, -1, -1):
    known = sum(m[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (m[i][-1] - known) / m[i][i]
    print(f"x{i + 1} = {x[i]}")
print("\n최종 결과")
for i, value in enumerate(x, start=1):
    print(f"x{i} = {value}")