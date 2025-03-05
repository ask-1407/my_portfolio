# 7-4:一時ファイルの活用

# TemporaryFile関数を使うとPython側がI/Oバッファ上に一時ファイルを作成できる。
import tempfile
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

