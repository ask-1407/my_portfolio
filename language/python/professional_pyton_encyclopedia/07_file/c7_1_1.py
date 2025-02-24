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