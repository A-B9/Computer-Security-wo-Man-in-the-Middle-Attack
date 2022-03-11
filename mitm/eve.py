import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = os.path.basename(sys.argv[0]).split('.', 1)[0]
mode = os.path.basename(sys.argv[0]).split('--')[1]

socket_alice, aes_alice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME) #connect to alice socket 
dialog.info('Connected to Alice as Bob.')
#Bob and alice will speak to each other through these sockets,
#I need to pass these messges from one socket to another.
socket_bob, aes_bob = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)#connect to bobs socket
dialog.info('Connected to Bob as Alice')

dialog.chat("Nice, getting there...")
received = receive_and_decrypt(aes_bob, socket_bob)
dialog.chat('Bob said: "{}"'.format(received))


if CUSTOM_CHAT:
    dialog.prompt('please input message...')
    to_send = input()
else:
    if mode == 'relay':
        to_send = received
    elif mode == 'break-heart'
        to_send = BAD_MSG['bob']
encrypt_and_send(to_send, aes_alice, socket_alice)
dialog.info('Message sent!')

tear_down(socket_alice, BUFFER_DIR, BUFFER_FILE_NAME)
tear_down(socket_bob, BUFFER_DIR, BUFFER_FILE_NAME)
