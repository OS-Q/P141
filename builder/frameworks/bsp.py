import sys
from os.path import basename, isdir, isfile, join

from SCons.Script import DefaultEnvironment

from platformio.proc import exec_command

env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("E122")
assert FRAMEWORK_DIR and isdir(FRAMEWORK_DIR)


env.Append(
    CPPPATH=[
        join(FRAMEWORK_DIR, "bsp"),
        join(FRAMEWORK_DIR, "lib"),
    ],
    LIBS=[
        "c"
    ]
)

libs = [
    env.BuildLibrary(
        join("$BUILD_DIR", "BSP"),
        join(FRAMEWORK_DIR, "bsp")),
    env.BuildLibrary(
        join("$BUILD_DIR", "LIB"),
        join(FRAMEWORK_DIR, "lib")),
]

env.Prepend(LIBS=libs)
