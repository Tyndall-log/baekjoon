def find(a, b, g, s, w, t, max_t):
	sum_g, sum_s, sum_m = 0, 0, 0
	i_max = len(g)
	for i in range(i_max):
		n = (t[i] + max_t) // (t[i] * 2)
		sum_g += min(g[i], w[i] * n)
		sum_s += min(s[i], w[i] * n)
		sum_m += min(g[i] + s[i], w[i] * n)
	print(sum_g, sum_s, sum_m)
	return a <= sum_g and b <= sum_s and a + b <= sum_m


def solution(a, b, g, s, w, t):
	left, right = 0, 10**5 * 10**9 * 2 * 2
	while left < right - 1:
		mid = (left + right) // 2
		r = find(a, b, g, s, w, t, mid)
		if r:
			right = mid
		else:
			left = mid
		print(mid)
	answer = left if find(a, b, g, s, w, t, left) else right
	return answer

print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))