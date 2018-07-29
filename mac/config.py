import sys
import os
import datetime
import subprocess

from keyhac import *


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 0:
        keymap.editor = "TextEdit"
        #keymap.editor = "Sublime Text 2"

    # Setting with callable object (Advanced usage)
    if 1:
        def editor(path):
            subprocess.call([ "open", "-a", "MacVim", path ])
        keymap.editor = editor


    # --------------------------------------------------------------------
    # 単純なキーの置き換え
    # --------------------------------------------------------------------

    # かな : 右Shift
    keymap.replaceKey( 104, "RShift" )


    # --------------------------------------------------------------------
    # ユーザモディファイアキーの定義
    # --------------------------------------------------------------------

    # 英数: User0
    keymap.defineModifier( 102, "User0" )


    # --------------------------------------------------------------------
    # グローバルキーマップの定義
    # --------------------------------------------------------------------
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # --------------------------------------------------------------------
        # ワンショットモディファイア

        # かな
        keymap_global["O-RShift"] = "(104)"
        # 英数
        keymap_global["O-(102)"] = "(102)"


        # --------------------------------------------------------------------
        # 単純なキーマップ

        # Shift, Ctrl などの修飾キーを含めた組み合わせを定義する
        for modify in ("", "Shift-", "Ctrl-", "Ctrl-Shift-", "Alt-", "Cmd-"):
            # User0 + H, J, K, L: ←↓↑→
            keymap_global[ modify + "User0-H" ] = modify + "Left"
            keymap_global[ modify + "User0-J" ] = modify + "Down"
            keymap_global[ modify + "User0-K" ] = modify + "Up"
            keymap_global[ modify + "User0-L" ] = modify + "Right"

            # User0 + A, E: Home, End
            keymap_global[ modify + "User0-A" ] = modify + "Home"
            keymap_global[ modify + "User0-E" ] = modify + "End"

            # User0 + F, V: PgDn, PgUp
            keymap_global[ modify + "User0-F" ] = modify + "PageDown"
            keymap_global[ modify + "User0-V" ] = modify + "PageUp"

        # User0 + B: BackSpace
        keymap_global[ "User0-B" ] = "Back"
        # User0 + D: Delete
        keymap_global[ "User0-D" ] = "Delete"

        # 簡単に矩形選択の画面キャプチャが取りたい
        # User0 + S: Command + Ctrl + Shift + 4
        keymap_global[ "User0-S" ] = "Cmd-Ctrl-Shift-4"

        # バックスラッシュをWindowsと同じように入力したい
        # _: \
        keymap_global[ "(94)" ] = "Alt-(93)"


        # --------------------------------------------------------------------
        # 画面サイズ変更 Spectacle

        # User0 + ↑: フルスクリーン
        keymap_global[ "User0-Up" ]    = "Alt-Cmd-O"
        # User0 + ←: 左半分
        keymap_global[ "User0-Left" ]  = "Alt-Cmd-H"
        # User0 + →: 右半分
        keymap_global[ "User0-Right" ] = "Alt-Cmd-L"

        # Vimと同じように、２ストロークで画面サイズを変更
        keymap_global[ "User0-W" ] = keymap.defineMultiStrokeKeymap("User0-W")
        # User0 + W > O: フルスクリーン
        keymap_global[ "User0-W" ][ "O" ] = "Alt-Cmd-O"
        # User0 + W > H,J, K, L: 左半分, 下半分, 上半分, 右半分
        keymap_global[ "User0-W" ][ "H" ] = "Alt-Cmd-H"
        keymap_global[ "User0-W" ][ "J" ] = "Alt-Cmd-J"
        keymap_global[ "User0-W" ][ "K" ] = "Alt-Cmd-K"
        keymap_global[ "User0-W" ][ "L" ] = "Alt-Cmd-L"

    # --------------------------------------------------------------------
    # 特定ウィンドウのアクティブ化／アプリケーションの実行
    # --------------------------------------------------------------------
    if 1:
        # User0 + 1 : Finder
        keymap_global[ "User0-1" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Finder" ], cwd=os.environ["HOME"] )
        # User0 + 2 : Safari
        keymap_global[ "User0-2" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Safari" ], cwd=os.environ["HOME"] )
        # User0 + 3 : Terminal
        keymap_global[ "User0-3" ] = keymap.ActivateApplicationCommand( app_name="com.apple.Terminal" )
        # User0 + 4／User0 + ; : MacVim
        keymap_global[ "User0-4" ]         = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "MacVim" ], cwd=os.environ["HOME"] )
        keymap_global[ "User0-Semicolon" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "MacVim" ], cwd=os.environ["HOME"] )
        # User0 + Space : Alfred
        # User0 + M : Google Keep
        keymap_global[ "User0-M" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Default hmjkmjkepdijhoojdojkdfohbdgmmhki.app" ], cwd=os.environ["HOME"] )
        # User0 + N : OneNote
        keymap_global[ "User0-N" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Microsoft OneNote" ], cwd=os.environ["HOME"] )
        keymap_global[ "User0-Space" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Alfred" ], cwd=os.environ["HOME"] )

    # --------------------------------------------------------------------
    # クリップボード関係
    # --------------------------------------------------------------------
    if 1:
        keymap_global[ "User0-Z" ] = keymap.command_ClipboardList

    # --------------------------------------------------------------------
    # 特定のウィンドウのキーマップの定義
    # --------------------------------------------------------------------
    if 1:
        # --------------------------------------------------------------------
        # Alfred
        keymap_alfred = keymap.defineWindowKeymap( app_name="com.alfredapp.Alfred" )

        # Ctrl + [: Escape
        keymap_alfred[ "Ctrl-CloseBracket" ] = "Escape"

        # --------------------------------------------------------------------
        # OneNote
        keymap_onenote = keymap.defineWindowKeymap( app_name="com.microsoft.onenote.mac" )

        # コピペとアンドゥ・リドゥは、Windowsと同じショートカットが使いたい
        keymap_onenote[ "Ctrl-C" ] = "Cmd-C"
        keymap_onenote[ "Ctrl-V" ] = "Cmd-V"
        keymap_onenote[ "Ctrl-X" ] = "Cmd-X"
        keymap_onenote[ "Ctrl-Z" ] = "Cmd-Z"
        keymap_onenote[ "Ctrl-Y" ] = "Cmd-Y"
        # Ctrl + [: Escape
        keymap_onenote[ "Ctrl-CloseBracket" ] = "Escape"

        # --------------------------------------------------------------------
        # Visual Stdio Code
        keymap_vscode  = keymap.defineWindowKeymap( app_name="com.microsoft.VSCode" )

        # コピペとアンドゥ・リドゥは、Windowsと同じショートカットが使いたい
        keymap_vscode[ "Ctrl-C" ] = "Cmd-C"
        keymap_vscode[ "Ctrl-V" ] = "Cmd-V"
        keymap_vscode[ "Ctrl-X" ] = "Cmd-X"
        keymap_vscode[ "Ctrl-Z" ] = "Cmd-Z"
        keymap_vscode[ "Ctrl-Y" ] = "Cmd-Y"
        # Ctrl + [: Escape
        keymap_vscode[ "Ctrl-CloseBracket" ] = "Escape"

        # --------------------------------------------------------------------
        # Safari
        keymap_safari  = keymap.defineWindowKeymap( app_name="com.apple.Safari" )

        # コピペとアンドゥ・リドゥは、Windowsと同じショートカットが使いたい
        keymap_safari[ "Ctrl-C" ] = "Cmd-C"
        keymap_safari[ "Ctrl-V" ] = "Cmd-V"
        keymap_safari[ "Ctrl-X" ] = "Cmd-X"
        keymap_safari[ "Ctrl-Z" ] = "Cmd-Z"
        keymap_safari[ "Ctrl-Y" ] = "Cmd-Y"
        # タブ操作
        keymap_safari[ "Ctrl-T" ] = "Cmd-T"
        keymap_safari[ "Ctrl-W" ] = "Cmd-W"
        keymap_safari[ "Ctrl-Shift-T" ] = "Cmd-Shift-T"
        # ページ内検索
        keymap_safari[ "Ctrl-F" ] = "Cmd-F"
        # リロード
        keymap_safari[ "Ctrl-R" ] = "Cmd-R"
        # アドレスバーにカーソルを移動
        keymap_safari[ "Ctrl-L" ] = "Cmd-L"
        # すべてのタブを表示
        keymap_safari[ "Ctrl-E" ] = "Shift-Cmd-(93)"
        # Ctrl + [: Escape
        keymap_safari[ "Ctrl-CloseBracket" ] = "Escape"

        # --------------------------------------------------------------------
        # Chrome
        keymap_chrome  = keymap.defineWindowKeymap( app_name="com.google.Chrome" )

        # コピペとアンドゥ・リドゥは、Windowsと同じショートカットが使いたい
        keymap_chrome[ "Ctrl-C" ] = "Cmd-C"
        keymap_chrome[ "Ctrl-V" ] = "Cmd-V"
        keymap_chrome[ "Ctrl-X" ] = "Cmd-X"
        keymap_chrome[ "Ctrl-Z" ] = "Cmd-Z"
        keymap_chrome[ "Ctrl-Y" ] = "Cmd-Y"
        # Ctrl + [: Escape
        keymap_chrome[ "Ctrl-CloseBracket" ] = "Escape"

