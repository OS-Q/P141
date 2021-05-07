import sys
from os.path import basename, isdir, isfile, join

from SCons.Script import DefaultEnvironment

from platformio.proc import exec_command

env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("E15")
assert isdir(FRAMEWORK_DIR)


env.Append(
    CFLAGS=["--opt-code-size"],
    CPPPATH=[
        join(FRAMEWORK_DIR, "bsp"),
        join(FRAMEWORK_DIR, "lib"),
        "$PROJECTSRC_DIR",
    ]
)


env.BuildSources(
    join("$BUILD_DIR", "BSP"),
    join(FRAMEWORK_DIR, "bsp"),
    join(FRAMEWORK_DIR, "lib")
)
