import sys
import os
import datetime

import pyauto
from keyhac import *

# --------------------------------------------------------------------
# Mac から Windows の Amazon WorkSpaces クライアントを利用する際のキーマップ
#
# NOTE:
#   あらかじめキーボード設定にて、以下の設定を行っておくこと
#       Option  -> Command (KeyhacでWindownsキーにマッピング)
#       Command -> Option  (Altキーとして利用)
#
#   理由はなるべくWindowsの一般的なキー配列に合わせたいため

def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "notepad.exe"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            shellExecute( None, "notepad.exe", '"%s"'% path, "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # Simple key replacement

    # Option -> Win
    # NOTE: キーボード設定で Option -> Command にしておくと、WorkSpaces上で左のOptionキーが右Ctrlになる
    keymap.replaceKey( "RCtrl", "LWin" )

    # --------------------------------------------------------------------
    # User modifier key definition

    # Space をモディファイアキーとして定義
    keymap.defineModifier( 32, "User0" )

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # Ctrl + h: <BackSpace>
        keymap_global[ "C-h" ] = "Back"
        # C + [: <Esc>
        keymap_global[ "C-(219)" ] = "Esc"

        # User0が単独で押されたときは、そのまま使用する
        keymap_global["O-(32)"] = "(32)"

        # Shift, Alt, Win + Space をそのまま使用する
        keymap_global[ "Shift-Space" ] = "Shift-Space"
        keymap_global[ "Alt-Space" ] = "Alt-Space"
        keymap_global[ "Win-Space" ] = "Win-Space"

        # Shift, Ctrl を含めた組み合わせを定義する
        for modify in ("", "Shift-", "Ctrl-", "Shift-Ctrl-"):
            # User0 + h: <Left>
            keymap_global[ modify + "U0-h" ] = modify + "Left"
            # User0 + j: <Down>
            keymap_global[ modify + "U0-j" ] = modify + "Down"
            # User0 + k: <Up>
            keymap_global[ modify + "U0-k" ] = modify + "Up"
            # User0 + l: <Right>
            keymap_global[ modify + "U0-l" ] = modify + "Right"

            # User0 + a: <Home>
            keymap_global[ modify + "U0-a" ] = modify + "Home"
            # User0 + e: <End>
            keymap_global[ modify + "U0-e" ] = modify + "End"

            # User0 + f: <PgDn>
            keymap_global[ modify + "U0-f" ] = modify + "PageDown"
            # User0 + v: <PgUp>
            keymap_global[ modify + "U0-v" ] = modify + "PageUp"

        # User0 + d: <Delete>
        keymap_global[ "U0-D" ] = "Delete"
