import pandas as pd
from io import StringIO

def csv(line, cell):
    # セル全体を格納する文字列を作成
    sio = StringIO(cell)
    # pandasのread_csv()を使ってCSVを読み込む
    return pd.read_csv(sio)

def load_ipython_extension(ipython):
    """拡張がロードされる際に、この関数が呼ばれる。
    パラメータとしてIPythonのInteractiveShellインスタンスが渡される。
    register_magic_function関数を呼び出して、magicコマンドを登録する。"""
    ipython.register_magic_function(csv, 'cell')