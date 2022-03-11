import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = os.path.basename(sys.argv[0]).split('.', 1)[0]#gets the name of the player from the command line input

os.rename(BUFFER_DIR+BUFFER_FILE_NAME,BUFFER_DIR+"eveFile")
socket_bob, aes_bob = setup('bob', BUFFER_DIR, "eveFile")#connect to bobs socket
socket_alice, aes_alice = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME) #connect to alice socket 

dialog.info('Connected to Alice as Bob.')
#Bob and alice will speak to each other through these sockets,
#I need to pass these messges from one socket to another.
dialog.info('Connected to Bob as Alice')
dialog.chat("Nice, getting there...")


received_from_Bob = receive_and_decrypt(aes_alice, socket_alice)
dialog.chat('Bob said: "{}"'.format(received_from_Bob))
if os.path.basename(sys.argv[1]) == '--custom':
    CUSTOM_CHAT = True

if CUSTOM_CHAT:
    dialog.prompt('please input message...')
    to_send = input()
else:
    if os.path.basename(sys.argv[1]) == '--relay':
        to_send = received_from_Bob
    elif os.path.basename(sys.argv[1]) == '--break-heart':
        to_send = BAD_MSG['bob']
encrypt_and_send(to_send, aes_bob, socket_bob)
dialog.info('Message sent!')
######################################################################

received_from_Alice = receive_and_decrypt(aes_bob, socket_bob)
dialog.chat('Alice said: "{}"'.format(received_from_Alice))

if CUSTOM_CHAT:
    dialog.prompt('please input message...')
    to_send = input()
else:
    if os.path.basename(sys.argv[1]) == '--relay':
        to_send = received_from_Alice
    elif os.path.basename(sys.argv[1]) == '--break-heart':
        to_send = BAD_MSG['alice']
encrypt_and_send(to_send, aes_alice, socket_alice)
dialog.info('Message sent!')

tear_down(socket_bob, BUFFER_DIR, "eveFile")
tear_down(socket_alice, BUFFER_DIR, BUFFER_FILE_NAME)