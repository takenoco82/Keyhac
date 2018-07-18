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

    # Space: 右Shift
    keymap.replaceKey( "Space", "RShift" )
    # かな : 右Ctrl
    keymap.replaceKey( 104, "RCtrl" )


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

        # 単独 および 修飾キーと一緒に押された場合
        for modify in ("", "Shift-", "Ctrl-", "Ctrl-Shift-", "Alt-", "Cmd-", "Cmd-Shift-"):
            # Space
            keymap_global[ "O-" + modify + "RShift" ] = modify + "Space"

        # かな
        keymap_global["O-RCtrl"] = "(104)"
        # 英数
        keymap_global["O-(102)"] = "(102)"


        # --------------------------------------------------------------------
        # 単純なキーマップ

        # Shift, Ctrl を含めた組み合わせを定義する
        for modify in ("", "Shift-", "Ctrl-", "Ctrl-Shift-"):
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
        keymap_global[ "User0-RShift" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Alfred" ], cwd=os.environ["HOME"] )
        # User0 + M : Google Keep
        keymap_global[ "User0-M" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Default hmjkmjkepdijhoojdojkdfohbdgmmhki.app" ], cwd=os.environ["HOME"] )
        # User0 + N : OneNote
        keymap_global[ "User0-N" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Microsoft OneNote" ], cwd=os.environ["HOME"] )

    # --------------------------------------------------------------------
    # クリップボード関係
    # --------------------------------------------------------------------
    if 1:
        keymap_global[ "User0-Z" ] = keymap.command_ClipboardList

