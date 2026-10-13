from fractions import Fraction

def print_matrix(name, m):
    #행렬을 보기 좋게 출력
    print(name)
    for row in m:
        print(f"[{" ".join(f"{str(v):>5}" for v in row)}]")
    print()

#주어진 행렬
a = [
    [1, 2, 1],
    [2, 3, 3],
    [-3, -10, 2]
]

n = len(a)

#U는 A의 복사본에서 시작한다.
#Fraction을 사용하여 분수를 정확하게 계산한다.
u = [[Fraction(v) for v in row] for row in a]

#L은 단위행렬에서 시작한다.
l = [
    [Fraction(1 if i == j else 0) for j in range(n)]
    for i in range(n)
]
print_matrix("초기 행렬 A", a)

#가우스 소거법: 피벗 아래의 원소를 0으로 만든다.
for k in range(n - 1):
    if u[k][k] == 0:
        raise ValueError("피벗이 0이므로 행 교환이 필요합니다.")

    for i in range(k + 1, n):
        #소거 배수 = 없앨 원소 / 피벗
        multiplier = u[i][k] / u[k][k]

        #소거 배수를 L에 저장
        l[i][k] = multiplier

        #Ri <- Ri - multiplier x Rk
        u[i] = [
            u[i][j] - multiplier * u[k][j]
            for j in range(n)
        ]

        print(f"R{i + 1} <- R{i + 1} - ({multiplier}) x R{k + 1}")
        print_matrix("현재 U", u)

print_matrix("최종 하삼각행렬 L", l)
print_matrix("최종 상삼각행렬 U", u)

#행렬 곱 LU 계산
lu = [
    [
        sum(l[i][k] * u[k][j] for k in range(n))
        for j in range(n)
    ]
    for i in range(n)
]

print_matrix("검산: L x U", lu)
print(f"LU = A 확인: {lu == a}")