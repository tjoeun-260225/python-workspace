import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.datasets import make_blobs

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

X, _ = make_blobs(n_samples=1000, centers=3, random_state=42)

fig, ax = plt.subplots(figsize=(7, 5))

def update(frame):
    ax.clear()
    ax.set_title(f'점 하나씩 추가 중 - {frame+1}/300개')

    # frame번째까지의 점만 찍기
    ax.scatter(X[:frame+1, 0], X[:frame+1, 1],
               c='steelblue', alpha=0.6, s=30)

    ax.set_xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
    ax.set_ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)

ani = animation.FuncAnimation(
    fig,
    update,
    frames=1000,   # 300개 점을 하나씩
    interval=20,  # 0.02초마다 (빠르게)
    repeat=False
)

plt.tight_layout()
plt.show()