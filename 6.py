import numpy as np
import matplotlib.pyplot as plt

#1. 회전각: 도(degree)를 라디안으로 변환
theta_deg = 60
theta = np.deg2rad(theta_deg)

#2. 시계 방향 회전정렬
a = np.array([
    [np.cos(theta), np.sin(theta)],
    [-np.sin(theta), np.cos(theta)]
])

#3. 각 열이 하나의 꼭짓점인 2x4행렬
#P1 = (1, 1), P2 = (1, 2), P3 = (2, 2), P4 = (2, 1)
p = np.array([
    [1, 1, 2, 2],
    [1, 2, 2, 1]
], dtype=float)

#4. 네 꼭짓점을 한 번에 변환
#(2x2) @ (2x4) = (2x4)
q = a @ p

np.set_printoptions(precision=4, suppress=True)

print(f"회전정렬 A:\n{a}")

print("\n각 꼭짓점의 변환 결과:")
for i in range(p.shape[1]):
    print(
        f"P{i + 1}: ({p[0, i]:.0f}, {p[1, i]:.0f})"
        f" -> ({q[0, i]:.4f}, {q[1, i]:.4f})"
    )

#5. 원점에서 각 꼭짓점까지의 거리 보존 확인
before = np.linalg.norm(p, axis=0)
after = np.linalg.norm(q, axis=0)

print(f"\n원점까지의 거리 보존: {np.allclose(before, after)}")

#6. 첫 꼭짓점을 끝에 추가하여 닫힌 정사각형으로 그린다.
p_closed = np.column_stack((p, p[:, 0]))
q_closed = np.column_stack((q, q[:, 0]))
fig, ax = plt.subplots(figsize=(7, 7))

ax.plot(
    p_closed[0], p_closed[1],
    "o-", color="royalblue", label="Original"
)
ax.plot(
    q_closed[0], q_closed[1],
    "o--", color="darkorange",
    label=f"Rotated {theta_deg} degrees colckwise"
)
#꼭짓점 이름 표시
for i in range(p.shape[1]):
    ax.annotate(
        f"P{i + 1}", p[:, i],
        xytext=(6, 8), textcoords="offset points"
    )
    ax.annotate(
        f"P{i + 1}'", q[:, i],
        xytext=(6, -16), textcoords="offset points"
    )
#원점에서 첫 꼭짓점으로 향하는 벡터 표시
for point, color in [(p[:, 0], "royalblue"),
                     (q[:, 0], "darkorange")]:
    ax.annotate(
        "", xy=point, xytext=(0, 0),
        arrowprops=dict(arrowstyle="->", color=color)
    )
ax.axhline(0, color="gray", linewidth=1)
ax.axvline(0, color="gray", linewidth=1)
ax.scatter(0, 0, color="black", zorder=5, label="Origin")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Rotation about the origin")
ax.set_aspect("equal", adjustable="box")
ax.margins(0.2)
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show()