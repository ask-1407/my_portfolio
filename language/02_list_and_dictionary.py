# 項目11 シーケンスをどのようにスライスするか知っておく

"""

"""

a = ['a','b','c','d','e','f','g','h']
# リストの先頭からスライスするときにはインデックスのゼロは省く。
assert a[:5] == a[0:5]
# 終端までスライスするときは末尾のインデックスは冗長になるので省く。
assert a[5:] == a[5:len(a)]

# スライスであれば指定値がリストの境界を超えていても出力される。
first_twenty_times = a[:20]
last_twenty_times = a[-20:]
print(first_twenty_times) # output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(last_twenty_times)

# ただし直接アクセスすると例外がでる
a[20] # IndexError: list index out of range


