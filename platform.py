from platform import system
from platformio.managers.platform import PlatformBase

class P141Platform(PlatformBase):
    def configure_default_packages(self, variables, target):
        return PlatformBase.configure_default_packages(self, variables,target)
