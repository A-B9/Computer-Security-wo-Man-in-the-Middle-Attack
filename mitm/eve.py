import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = os.path.basename(sys.argv[0]).split('.', 1)[0]
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)

