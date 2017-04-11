import sys
import os
import datetime
import subprocess

from keyhac import *


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "TextEdit"
        #keymap.editor = "Sublime Text 2"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            subprocess.call([ "open", "-a", "TextEdit", path ])
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
        for modify in ("", "Shift-", "Ctrl-", "Ctrl-Shift-", "Alt-", "Cmd-Shift-"):
            # Space
            keymap_global[ "O-" + modify + "RShift" ] = modify + "Space"

        # command + Space で Alfred を実行する
        keymap_global[ "O-Cmd-RShift" ] = keymap.SubProcessCallCommand( cmd=[ "open", "-a", "Alfred" ], cwd=os.environ["HOME"] )

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

        # User0 + C, V, X: コピー, 貼り付け, 切り取り
        keymap_global[ "User0-C" ] = "Cmd-C"
        keymap_global[ "User0-V" ] = "Cmd-V"
        keymap_global[ "User0-X" ] = "Cmd-X"

        # User0 + U, R: Undo, Redo
        keymap_global[ "User0-U" ] = "Cmd-Z"
        keymap_global[ "User0-R" ] = "Cmd-Y"


        # --------------------------------------------------------------------
        # 画面サイズ変更 Spectacle

        # User0 + ↑: フルスクリーン
        keymap_global[ "User0-Up" ]    = "Alt-Cmd-F"
        # User0 + ←: 左半分
        keymap_global[ "User0-Left" ]  = "Alt-Cmd-H"
        # User0 + →: 右半分
        keymap_global[ "User0-Right" ] = "Alt-Cmd-L"


    # --------------------------------------------------------------------
    # 特定ウィンドウのアクティブ化
    # --------------------------------------------------------------------
    if 1:
        # User0 + 1 : Finder
        keymap_global[ "User0-1" ] = keymap.ActivateApplicationCommand( app_name="com.apple.finder" )
        # User0 + 2 : Safari
        keymap_global[ "User0-2" ] = keymap.ActivateApplicationCommand( app_name="com.apple.Safari" )
        # User0 + 3 : Terminal
        keymap_global[ "User0-3" ] = keymap.ActivateApplicationCommand( app_name="com.apple.Terminal" )
        # User0 + 4 : OneNote
        keymap_global[ "User0-4" ] = keymap.ActivateApplicationCommand( app_name="com.microsoft.onenote.mac" )
