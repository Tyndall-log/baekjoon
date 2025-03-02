import sys
pin = sys.stdin.readline


if __name__ == "__main__":
	N, M, dice_i, dice_j, K = map(int, pin().split())
	dice = [0] * 6
	grid = [list(map(int, pin().split())) for _ in range(N)]
	K_list = list(map(int, pin().split()))
	direction = list(zip([0, 0, -1, 1], [1, -1, 0, 0]))  # i, j
	result = []

	def rotate(direction):
		if direction == 1:  # 동
			dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
		elif direction == 2:  # 서
			dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
		elif direction == 3:  # 북
			dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
		elif direction == 4:  # 남
			dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

	for k in K_list:
		di, dj = direction[k-1]
		ii, jj = dice_i + di, dice_j + dj
		if not (0 <= ii < N and 0 <= jj < M):
			continue
		dice_i, dice_j = ii, jj
		rotate(k)
		if grid[ii][jj] == 0:
			grid[ii][jj] = dice[0]
		else:
			dice[0] = grid[ii][jj]
			grid[ii][jj] = 0
		result.append(dice[5])
	print(*result, sep='\n')
