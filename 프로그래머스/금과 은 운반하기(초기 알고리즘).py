import heapq


def x_to_sgm_sort(x1, x2, x):
	if x <= x1:
		return 0, 0, x
	if x <= x2:
		return 0, x - x1, x1
	k = x1 + x2
	if x < k:
		return x - x2, x - x1, k - x
	return x1, x2, 0


def x_to_sgm(s, g, x):
	if s < g:
		return x_to_sgm_sort(s, g, x)
	else:
		g, s, m = x_to_sgm_sort(g, s, x)
		return s, g, m


def solution(a, b, g, s, w, t):
	answer = -1
	i_max = len(g)
	c_s = [0 for i in range(i_max)]
	c_g = [0 for i in range(i_max)]
	c_m = [0 for i in range(i_max)]
	c_w = [0 for i in range(i_max)]
	ct_hq = [[t[i], i] for i in range(i_max)]
	heapq.heapify(ct_hq)
	ans_t = 0
	c_s_all = 0
	c_g_all = 0
	c_m_all = 0
	while True:
		c_t, c_i = heapq.heappop(ct_hq)
		heapq.heappush(ct_hq, [c_t + t[c_i] * 2, c_i])
		c_w[c_i] += w[c_i]
		_s, _g, _m = x_to_sgm(s[c_i], g[c_i], c_w[c_i])
		c_s_all += _s - c_s[c_i]
		c_g_all += _g - c_g[c_i]
		c_m_all += _m - c_m[c_i]
		c_s[c_i], c_g[c_i], c_m[c_i] = _s, _g, _m
		ans_t = c_t
		if (max(0, a - c_g_all) + max(0, b - c_s_all) - c_m_all <= 0):
			break

	return ans_t