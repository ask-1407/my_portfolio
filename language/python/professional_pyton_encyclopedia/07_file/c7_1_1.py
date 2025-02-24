# ファイル作成：writeメソッドでファイルを書き込み、closeメソッドでファイルを閉じる
f = open('test.txt','w')
f.write('test')
f.close()

# もともとテキストファイルがある場合、上書きされる
f = open('test.txt','w')
f.write('Test')
f.close()

# 追記の場合、open()メソッドの引数を'a'にする。
f = open('test.txt','a+')
f.write('Test')
f.close()

# with文を使えばcloseの記述が不要。open()を利用した際はclose()がないと閉じ忘れとなる。
with open('test.txt','w') as f:
    f.write('Test')


s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt','w') as f:
    f.write(s)

# 引数'r'を指定するとファイルの中身を読み込み変数に格納することができる。
with open('test.txt', 'r') as f:
    print(f.read())

# readlineメソッドとwhileループで一行ずつ読み込むことができる
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='') # デフォルトでは改行込み
        if not line: # 読み込む行がないと空
            break

# read()メソッドを利用すると、指定した塊毎に読むこともできる。
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

# tellメソッドを使うと現在ファイル内のどの場所を指しているかがわかる。
with open('test.txt','r') as f:
    print(f.tell())  # output : 0
    print(f.read(1)) # output :A

# seekメソッドを使うとファイルの特定の場所に移動できる。
with open('test.txt', 'r') as f:
    f.seek(5)
    print(f.read(1)) # output B

# 書き込みと読み込みを同時に行うときにはモードを'w+'と指定する。
# 'w+'でファイルをopenするとファイルを開いた直後は中身が空になっているので注意。
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0) # 書き込み後はファイルの位置が最後になっているので先頭に戻す。
    print(f.read())

# 'r+'でopenしたときは最初のファイルが読み込めないとエラーになる。
with open('test2.txt','r+') as f:
    print(f.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'test2.txt' 
    f.seek(0)
    f.write(s)
