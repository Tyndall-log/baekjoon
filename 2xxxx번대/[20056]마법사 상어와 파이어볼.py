import sys
pin = sys.stdin.readline


if __name__ == "__main__":
	N, M, K = map(int, pin().split())
	grid = [[[] for _ in range(N)] for _ in range(N)]
	for _ in range(M):
		r, c, m, s, d = list(map(int, pin().split()))
		grid[r - 1][c - 1].append([m, s, d])
	direction = list(zip([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]))

	for k in range(K):
		new_grid = [[[] for _ in range(N)] for _ in range(N)]
		# 이동
		for i in range(N):
			for j in range(N):
				for m, s, d in grid[i][j]:
					di, dj = direction[d]
					ii, jj = (i + di * s) % N, (j + dj * s) % N
					new_grid[ii][jj].append([m, s, d])
		grid = new_grid

		# 복사
		for i in range(N):
			for j in range(N):
				if len(grid[i][j]) < 2:
					continue
				m_sum = 0
				s_sum = 0
				dd = [0, 0]
				for m, s, d in grid[i][j]:
					m_sum += m
					s_sum += s
					dd[d % 2] += 1
				new_m = m_sum // 5
				new_s = s_sum // len(grid[i][j])
				grid[i][j].clear()
				if new_m <= 0:
					continue
				for d in ([0, 2, 4, 6] if dd[0] == 0 or dd[1] == 0 else [1, 3, 5, 7]):
					grid[i][j].append([new_m, new_s, d])

	# 출력
	sum_m = 0
	for i in range(N):
		for j in range(N):
			for m, s, d in grid[i][j]:
				sum_m += m
	print(sum_m)
