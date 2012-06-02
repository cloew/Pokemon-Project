from distutils.core import setup
import py2exe
import os
import sys


if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.6.1"
        self.company_name = "No Company"
        self.copyright = "no copyright"
        self.name = "py2exe sample files"
        
        
pkmn = Target(
    # used for the versioninfo resource
    description = "A sample GUI app",

    # what to build
    script = "main.py",
    icon_resources = [(1, "resources/images/pokeball.ico")],
    dest_base = "Pokemon")

setup(zipfile = None,
         windows=[pkmn],
         )