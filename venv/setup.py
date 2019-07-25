from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["instapy","tkinter","sys","tkinter.ttk", "tkinter.messagebox"],
	excludes = ["tkinter"])

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = [Executable("gui_tkinter.py", base=base)]

# 3
setup(
    name='Test Application',
    version = '0.1',
    author = "yewon",
    description = "I'M yewon!",
    options = dict(build_exe = buildOptions),
    executables = exe
)