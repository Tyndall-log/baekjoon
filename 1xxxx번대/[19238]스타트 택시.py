import sys
from collections import deque
pin = sys.stdin.readline


if __name__ == "__main__":
	N, M, fuel = map(int, pin().split())
	grid = [list(map(int, pin().split())) for _ in range(N)]
	grid2 = [grid[i][:] for i in range(N)]
	car_i, car_j = map(int, pin().split())
	car_i -= 1
	car_j -= 1
	customer_id = 0
	destination = []
	for i in range(M):
		si, sj, ei, ej = map(int, pin().split())
		grid[si - 1][sj - 1] = 2 + customer_id
		destination.append((ei - 1, ej - 1))
		customer_id += 1
	direction = list(zip([-1, 0, 1, 0], [0, 1, 0, -1]))  # i, j

	def bfs(grid, find_list):
		find_car_count = 0
		find_car_max = len(find_list)
		q = deque()
		q.append([(car_i, car_j), 0])
		visit = set()
		result = []
		while q:
			(i, j), move = q.popleft()
			if not (0 <= i < N and 0 <= j < N):
				continue
			if (i, j) in visit:
				continue
			visit.add((i, j))
			v = grid[i][j]
			if v == 1:
				continue
			if v in find_list:
				find_car_count += 1
				result.append([move, (i, j), v])
				if find_car_max <= find_car_count:
					break
			for d in range(4):
				di, dj = direction[d]
				q.append([(i + di, j + dj), move + 1])
		return result

	start_car_id_list = list(range(2, M + 2))
	for t in range(M):
		# 승객 태우러 출발지 가기
		find = bfs(grid, start_car_id_list)
		if not find:
			fuel = -1
			break
		move, (i, j), car_id = sorted(find)[0]
		start_car_id_list.remove(car_id)
		grid[i][j] = 0
		car_i, car_j = i, j
		fuel -= move
		if fuel < 0:
			break

		# 승객 목적지에 데려다 주기
		dest_i, dest_j = destination[car_id - 2]
		grid2[dest_i][dest_j] = -1
		find = bfs(grid2, [-1])
		if not find:
			fuel = -1
			break
		move, (i, j), car_id = find[0]
		car_i, car_j = i, j
		grid2[dest_i][dest_j] = 0
		fuel -= move
		if fuel < 0:
			break
		fuel += move * 2
	print(max(-1, fuel))
