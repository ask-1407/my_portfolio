# 値の判定
is_ok = 0

if is_ok: # 0以外の数値ならTrueとなる
    print('OK') # 
else:
    print('NO')

is_ok = ''

if is_ok: # 空の文字列ならFalse
    print('OK') # 
else:
    print('NO')

# Noneを判定するテクニック

is_empty = None
if is_empty is None: # Noneであることを判定
    print('None')

if is_empty is not None: # Noneでないことを判定
    print('None')

# 複数のリストをまとめるときにはZIP関数が使える
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple','banana','beer']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip[days, fruits, drinks]:
    print(day, fruit, drink)
