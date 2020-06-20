import sys
import os
import datetime

import pyauto
from keyhac import *

# --------------------------------------------------------------------
# NiZ で Windows の Amazon WorkSpaces クライアントを利用する際のキーマップ
#

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

    # NumLock (左Fn) -> 255 ユーザモディファイキーにするため
    keymap.replaceKey("NumLock", 255)
    # Insert -> 左Option
    keymap.replaceKey("Insert", "LWin")

    # --------------------------------------------------------------------
    # User modifier key definition

    # 255(左Fn) をモディファイアキーとして定義
    keymap.defineModifier(255, "User0")

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # 右Ctrlが単独で押されたときは、「変換」
        keymap_global["O-RCtrl"] = "(28)"
        # 255(左Fn)が単独で押されたときは、「無変換」
        keymap_global["O-(255)"] = "(29)"

        # Ctrl + h: <BackSpace>
        keymap_global["Ctrl-h"] = "Back"
        # Ctrl + m: <Enter>
        keymap_global["Ctrl-m"] = "Enter"
        # Ctrl + [: <Esc>
        keymap_global["Ctrl-OpenBracket"] = "Esc"

        # Shift, Ctrl を含めた組み合わせを定義する
        for modify in ("", "Shift-", "Ctrl-", "Shift-Ctrl-"):
            # User0 + h: <Left>
            keymap_global[ modify + "User0-h" ] = modify + "Left"
            # User0 + j: <Down>
            keymap_global[ modify + "User0-j" ] = modify + "Down"
            # User0 + k: <Up>
            keymap_global[ modify + "User0-k" ] = modify + "Up"
            # User0 + l: <Right>
            keymap_global[ modify + "User0-l" ] = modify + "Right"

            # User0 + a: <Home>
            keymap_global[ modify + "User0-a" ] = modify + "Home"
            # User0 + e: <End>
            keymap_global[ modify + "User0-e" ] = modify + "End"

            # User0 + f: <PgDn>
            keymap_global[ modify + "User0-f" ] = modify + "PageDown"
            # User0 + v: <PgUp>
            keymap_global[ modify + "User0-v" ] = modify + "PageUp"

        # User0 + d: <Delete>
        keymap_global[ "User0-D" ] = "Delete"

    # Customizing clipboard history list
    if 1:
        # Disable clipboard monitoring hook (Default:Enabled)
        keymap.clipboard_history.enableHook(False)
