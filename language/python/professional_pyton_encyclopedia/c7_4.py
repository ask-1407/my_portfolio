# 7-4:一時ファイルの活用

# TemporaryFile関数を使うとPython側がI/Oバッファ上に一時ファイルを作成できる。
import tempfile
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 実際に一時ファイルを作成したいときはNamedTemporaryFile関数を使う
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name) # 一時ファイルのパスを取得
    with open(t.name, 'w') as f:
        f.write('test')  

# 一時ディレクトリを作成するにはTemporaryDirectory関数を使う
with tempfile.TemporaryDirectory() as td:
    print(td) # 一時ディレクトリのパスを取得
temp_dir = tempfile.mkdtemp()

# 標準ライブラリのsuboprocessを使うとターミナル用のコマンドをPython上で実行できる。
import subprocess
subprocess.run(['ls', '-l'])

# run関数に引数にshell=Trueを指定するとリストを使わずに文字列コマンドを実行できる。
# LinuxやShellに詳しい人でないと難しいためコマンドがシンプルならリストを推奨する
subprocess.run('ls -al', shell=True)