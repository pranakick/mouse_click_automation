import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

switcher_key = KeyCode(char='y') #set up the hotkey for script activation
click_activity = False # the flag for click activity
mouse = Controller()


def clicker():
    while True:
        if click_activity:
            mouse.click(Button.left, 1)
            time.sleep(0.1)


def switcher(key):
    if key == switcher_key:
        global click_activity
        click_activity = not click_activity

#control and activation statement
def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=switcher) as listener:
        listener.join()


if __name__ == '__main__':
    main()