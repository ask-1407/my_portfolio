# 第三章 関数

# 項目19 複数の戻り値では4個以上の変数なrアンパックしない

"""
関数で複数の値を返すにはそれらをタプルにいれて呼び出し側でアンパック構文を使える。
関数からの複数の戻り値はcatch-allのアスタリスク付き引数でアンパックですることも可能。
4個以上の変数をアンパックするのはエラーになりやすいのでさける。
代わりに軽量なクラスかnamedtupleを利用する。
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths) # 呼び出しのコードが返されたタプルをアンパックして2つの変数に代入する。
print(f'Min: {minimum}, Max: {maximum}')# Min: 60, Max: 73


# catch-allアンパックのアスタリスク付き式でも複数の値を受け取ることができる。
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return average, scaled

longest, *middle, shortest = get_avg_ratio(lengths)

# 平均値，中央値，母集団のサイズを求められるように拡張。
"""
以下のコードの問題点
- 戻り値が全て数値なので，順序を間違えやすい。
- 値をアンパックする行が長くなり様々な方法で改行し続ける方法があるが，読みにくくなる。

そのため，四個以上の戻り値はアンパックせずに軽量クラスやnamedtupleを定義し，関数でそのインスタンスを返すようにする。
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count



        

            



            