from keyhac import *
import re

def configure(keymap):

    # --------------------------------------------------------------------
    # config.py編集用のテキストエディタの設定
    # --------------------------------------------------------------------

    # プログラムのファイルパスを設定 (単純な使用方法)
    if 1:
        keymap.editor = u"notepad.exe"

    # 呼び出し可能オブジェクトを設定 (高度な使用方法)
    if 0:
        def editor(path):
            shellExecute(
                    None,
                    None,
                    u"notepad.exe "%s"'% path,
                    "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # 単純なキーの置き換え
    # --------------------------------------------------------------------

    # 変換: Shift
    keymap.replaceKey( 28, "RShift" )

    # --------------------------------------------------------------------
    # ユーザモディファイアキーの定義
    # --------------------------------------------------------------------

    # 無変換: User0
    keymap.defineModifier( 29, "User0" )

    # --------------------------------------------------------------------
    # グローバルキーマップの定義
    # --------------------------------------------------------------------
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # 単独で押されたときは、BackSpace
        keymap_global["O-(28)"] = "Back"

        # User0が単独で押されたときは、無変換
        keymap_global["O-(29)"] = "(29)"

        # Shift, Ctrl を含めた組み合わせを定義する
        for modify in ("", "S-", "C-", "C-S-"):
            # User0 + h: <Left>
            keymap_global[ modify + "U0-H" ] = modify + "Left"
            # User0 + j: <Down>
            keymap_global[ modify + "U0-J" ] = modify + "Down"
            # User0 + k: <Up>
            keymap_global[ modify + "U0-K" ] = modify + "Up"
            # User0 + l: <Right>
            keymap_global[ modify + "U0-L" ] = modify + "Right"

            # User0 + a: <Home>
            keymap_global[ modify + "U0-A" ] = modify + "Home"
            # User0 + e: <End>
            keymap_global[ modify + "U0-E" ] = modify + "End"

            # User0 + f: <PgDn>
            keymap_global[ modify + "U0-F" ] = modify + "PageDown"
            # User0 + v: <PgUp>
            keymap_global[ modify + "U0-V" ] = modify + "PageUp"

        # User0 + b: <BackSpace>
        keymap_global[ "U0-B" ] = "Back"
        # User0 + d: <Delete>
        keymap_global[ "U0-D" ] = "Delete"
        # User0 + w: <S-C-Left><C-x>
        keymap_global[ "U0-W" ] = "S-C-Left","C-X"
        # User0 + u: <S-Home><C-x>
        keymap_global[ "U0-U" ] = "S-Home","C-X"

        # User0 + p: <M-Esc>
        keymap_global[ "U0-P" ] = "A-Esc"
        # Shift + User0 + n: <M-Esc>
        keymap_global[ "S-U0-N" ] = "A-Esc"
        # User0 + n: <M-S-Esc>
        keymap_global[ "U0-N" ] = "A-S-Esc"

        # C + [: <Esc>
        keymap_global[ "C-(219)" ] = "Esc"

        # <Ctrl><Ctrl>
        #keymap_global[ "Ctrl" ] = keymap.defineMultiStrokeKeymap( "Ctrl" )
        #keymap_global[ "S-Insert" ] = shellExecute(None, None, u"C:/Users/admin/local/bin/fenrir075c/fenrir.exe", '', u"C:/Users/admin/local/bin/fenrir075c")

        # @shellExecuteのラッパーメソッド
        # @param path:    実行ファイルのパス
        # @param param:   パラメータ
        # @param workdir: 起動ディレクトリ
        #def launcher(path, param = u"", workdir = u""):
        #    if workdir == u"":
        #        workdir = re.sub(ur"\\[^\\]*$", ur"", path)
        #    def _launcher():
        #        if path != u"":
        #            shellExecute(None, None, path, param, workdir, SW_NORMAL)
        #    return _launcher

        # User0 + y: eClipの起動
        #keymap_global[ "U0-Y" ] = launcher(ur"E:\home\admin\bin\eClip\eClip.exe")

        # User0 + z: ウィンドウの最小化
        #keymap_global[ "U0-Z" ] = minimize

