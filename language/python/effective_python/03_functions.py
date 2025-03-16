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

# 項目20 Noneを返すのではなく例外を送出する。
"""
- Noneを返して特別な意味を示す変数はNoneと他の値とが全て条件式においてFalseに評価されるため，エラーを引き起こしやすい。
- Noneを返す代わりに例外を送出することで特別な条件を示すようにする。
- 型ヒントを使って関数が特別な場合にもで絶対にNoneを返さないことを明示できる。
"""

# 例えば以下のようなある数を別の数で割るヘルパー関数を考える。
def careful_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

# この関数を使うコードは戻りに応じて振る舞いを変える
x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

# ただし分子がゼロの場合を考えると面倒なことになる。
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs') # 返り値がNoneで上述のifがFalseと判定されてしまい，ここの出力がされてしまう。

# このようなエラーを減らす方法は2つある。
# 1: 戻り値を2値のタプルにする。第一項は演算の成功・失敗を，第二稿は計算された実際の結果を返す。

def careful_divide(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

# この関数の返り値はタプルをアンパックする必要があるため，除算の結果だけでなく状態をい考慮させることができる。 
success, result = careful_divide(x, y)
if not success:
    print('Invalid inputs')

# しかし，呼び出し元がタプルの最初の部分を無視することができるので抜け穴になっている。
_, result = careful_divide(x, y)
if not result:
    print('Invalid inputs')


# 2: 特別な場合にはそもそもNoneを返さず例外を呼び出し元に送出する。
def careful_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') 

x,y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result) # Result is 2.5

# この方法は型ヒントを使ったコードにも拡張できる。入力・出力・例外が明確になり呼び出し元を間違える回数がかなり減る。
def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    
    Raises:
        ValueError: When inputs cannot be divided.
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')

# 項目21 クロージャが変数スコープとどう関わるかを把握する。
"""
クロージャ関数は定義されたスコープのどれからでも変数を参照できる。
デフォルトではクロージャ内での変数への代入は外部のスコープには影響しない
nonlocal文を用いて，クローじゅあが外のスコープにある変数を修正できる
nonlocal文を単純な関数でのみ使う要にする
"""

def sort_priority(numbers, group):# 一部の数を優先してソートする。
    def helper(x):
        if x in group:
            return(0, x)
        return (1, x)
    numbers.sort(key = helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = [2, 3, 5, 7]
sort_priority(numbers, group) # >>> [2, 3, 5, 7, 1, 4, 6, 8]

# この関数が期待通りに動く理由
"""
1. Pythonがクロージャ(定義されたスコープの変数を参照する関数)をサポートしている
2. Pythonでは関数がファーストクラスオブジェクトである＝直接参照でき，変数に代入したり他の関数に引数として渡せる。
3. Pythonはタプルを含めたシーケンスの比較に特別な規則を持つ。
"""

# 優先してほしい要素があったらフラグを立てるようにしたいとして，以下のように実装する。
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return(0, x)
        return (1, x)
    numbers.sort(key = helper)
    return found

found = sort_priority2(numbers, group)
print('Found:' found) # Found: false
print(numbers) # >>> [2, 3, 5, 7, 1, 4, 6, 8]

"""
ソートした結果は正しいがフラグはFalseとなる。
変数foundはhelper関数のスコープには存在しなかったため，Pythonが新たな変数として定義した。
そのためsort_priority2関数の変数foundはFalseのままでReturnされた。
一見面食らうが，スコープが定められているおかげで，ローカル変数が他から汚染されずにすんでいる。
"""

# Pythonではnonlocal文が指定した変数の代入に際してスコープ横断すべきことを示す。ただしモジュールレベルのスコープまではいかない。

def sort_priority(numbers, group):
    found = False
    def helper(x):
        nonlocal found # クロージャの外にあることを示す。ただし副作用の原因になるのでそこは注意。
        if x in group:
            found = True
            return(0, x)
    return(1, x)
    numbers.sort(key = helper)
    return found

# nonlocalの使い方が複雑になってきたら状態をヘルパークラスでラップするとよい。
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = found
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return(0, x)
        return(1, x)

# 項目22 可変長位置帰趨を使って見た目をすっきりさせる。
"""
関数は" *args" を使うことで可変個数の位置引数を受け入れることができる。
*演算子を関数に用いてシーケンスからの要素を位置引数とそして使える
*演算子をジェネレータと一緒に使うとプログラムがメモリを使い果たしてクラッシュすることがある
*argsを使う関数に新たに位置パラメータを追加すると 発見が困難なバグを生む可能性がある
"""

# 可変長位置引数を用いると関数呼び出しがより明確になる。

# 以下の関数を題材にする。現状では，値がなくても空のリストを渡さないといけないのが面倒。
def log(message,values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('My numbers are',[1,2])
log('My numbers are', [1, 2]) # My numbers are: 1, 2
log('Hi there', []) # Hi there


# valuesを可変長位置引数とすると，それが実現できる。シーケンスでlogのような可変個引数関数を呼び出したいなら*演算子を使えば呼び出せる。
def log(message,*values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('My numbers are',[1,2])

log('My numbers are', 1, 2) # My numbers are: 1, 2
log('Hi there') # Hi there

# ただし注意点もある
"""
1. 可変個数の引数が関数に渡される前に常にタプルに変換される

関数の呼び出し元がジェネレータで*演算子を使うと終わるまでイテレーションされる。
結果のタプルにはすべてのジェネレータからの値が含まれるのでメモリを大量に消費してプログラムをクラッシュさせる。
引数リストの入力個数が少ないことがわかっている場合が一番適している。
"""

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it) # >>> (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

"""
2. 全ての呼び出し元を修正せずには関数に対して新たな位置引数を追加できない。

"""
def log(sequence, message, *values): # 
    if not values:
        print(f'{sepuence} - {message}')
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{sepuence} - {message}: {values_str}')

# 更新前の呼び出し方ではNG
log('Favorite numbers', 7, 33) # >>> Favorite numbers -7:33 

# 上記例の場合，例外を起こさずに実行続けるので探し出すのが困難。*argsを受け入れる関数を拡張したいときにはキーワード専用引数を使うとよい。