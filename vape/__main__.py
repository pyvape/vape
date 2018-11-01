import sys

from vape.halo import Halo
from cleo import Application

vape = Application()
vape.add(Halo())


sys.exit(vape.run())
