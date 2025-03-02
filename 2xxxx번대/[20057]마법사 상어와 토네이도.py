import sys
import math
pin = sys.stdin.readline


if __name__ == "__main__":
	N = int(pin())
	grid = [list(map(int, pin().split())) for _ in range(N)]
	tornado = [
		(-2, 0, 0.02),
		(-1, -1, 0.10),
		(-1, 0, 0.07),
		(0, -2, 0.05),
		(-1, 1, 0.01),
		(1, -1, 0.10),
		(1, 0, 0.07),
		(1, 1, 0.01),
		(2, 0, 0.02),
	]
	tornado_direction = [tornado]
	for _ in range(3):
		new_td = []
		for i, j, p in tornado_direction[-1]:
			new_td.append((-j, i, p))
		tornado_direction.append(new_td)

	move_direction = list(zip([0, 1, 0, -1], [-1, 0, 1, 0]))  # i, j

	i, j = N // 2, N // 2
	mk, k, d = 0, 0, 3
	out = 0
	for n in range(N * N - 1):
		# 토네이도 중심 계산
		if k == 0:
			if d % 2 == 1:
				mk += 1
			d = (d + 1) % 4
			k = mk
		k -= 1
		di, dj = move_direction[d]
		i += di
		j += dj

		# 모래 날리기
		target = grid[i][j]
		grid[i][j] = 0
		alpha = target
		td = tornado_direction[d]
		for ti, tj, p in td:
			tar_i, tar_j = i + ti, j + tj
			sand = math.floor(target * p)
			if 0 <= tar_i < N and 0 <= tar_j < N:
				grid[tar_i][tar_j] += sand
			else:
				out += sand
			alpha -= sand
		alpha_i, alpha_j = i + di, j + dj
		if 0 <= alpha_i < N and 0 <= alpha_j < N:
			grid[alpha_i][alpha_j] += alpha
		else:
			out += alpha
	print(out)
