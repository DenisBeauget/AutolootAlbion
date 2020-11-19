from cx_Freeze import setup, Executable

# Setup project
setup(
    name = "autoloot",
    version = "0.1",
    description = "This script help you to do your PNJ in Albion Online",
    executables = [Executable("autoloot.py")],
)