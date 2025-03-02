import sys
from collections import deque
pin = sys.stdin.readline


if __name__ == "__main__":
	N, M = map(int, pin().split())
	grid = [list(map(int, pin().split())) for _ in range(N)]
	direction = list(zip([-1, 0, 1, 0], [0, 1, 0, -1]))  # i, j

	def gravity():
		grid_t = list(map(list, zip(*grid)))
		for j in range(N):
			col = grid_t[j]
			new_col = [-2 for _ in range(N)]
			find_m1 = [-1]
			for i in range(N):
				if col[i] == -1:
					find_m1.append(i)
					new_col[i] = -1
			find_m1.append(N)
			for k in range(len(find_m1) - 1):
				s = find_m1[k] + 1
				e = find_m1[k + 1]
				i = e - 1
				for t in range(e - 1, s - 1, -1):
					if 0 <= col[t]:
						new_col[i] = col[t]
						i -= 1
			for i in range(N):
				grid[i][j] = new_col[i]

	def find_group():
		group_id_grid = [[-1] * N for _ in range(N)]
		id_count = 0
		id_data_list = []  # [총 갯수, 무지개 갯수, (i, j), 블록 그룹]

		def bfs(idc, i, j, v):
			if not (0 <= i < N and 0 <= j < N):
				return
			if 0 <= group_id_grid[i][j]:
				return
			block = grid[i][j]
			data = id_data_list[idc]
			if block <= -1:
				return
			elif block == 0:
				data[1] += 1
			elif block == v:
				group_id_grid[i][j] = idc
			else:
				return
			data[0] += 1
			data[3].append((i, j))
			for d in range(4):
				di, dj = direction[d]
				if (i + di, j + dj) not in data[3]:
					bfs(idc, i + di, j + dj, v)

		for i in range(N):
			for j in range(N):
				block = grid[i][j]
				if 0 < block and group_id_grid[i][j] < 0:
					id_data_list.append([0, 0, (i, j), []])
					id_count += 1
					bfs(id_count - 1, i, j, block)
		if not id_data_list:
			return
		# print("id_data_list", id_data_list)
		return sorted(id_data_list)[-1]

	def ccw(grid):
		return list(map(list, zip(*grid)))[::-1]

	def remove_block(history):
		for i, j in history:
			grid[i][j] = -2

	def show(s):
		print(s)
		for i in range(N):
			for j in range(N):
				print(f'{(grid[i][j] if grid[i][j] >= -1 else "."):>2}', end='')
			print()

	# 오토 플레이
	score = 0
	while True:
		r = find_group()
		if not r:
			break
		count, _, (i, j), history = r
		if count < 2:
			break
		score += count ** 2
		print("count", count)
		show("grid1")
		remove_block(history)
		show("grid2")
		gravity()
		show("grid3")
		grid = ccw(grid)
		show("grid4")
		gravity()
	print(score)