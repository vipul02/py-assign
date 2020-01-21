nums = [12,24,35,24,88,120,155,88,120,155]
res = set()
print([_ for _ in nums if _ not in res and not res.add(_)][::-1])