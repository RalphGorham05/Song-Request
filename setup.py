__author__ = 'Jarrod'

import sys
from cx_Freeze import setup, Executable



base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Form Fill",
        version = "0.1",
        description = "My Form application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("kivytest.py", base=base)])
