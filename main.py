import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

"""
variables to control delay, mouse click, and start / stop buttons
"""
delay = 0.00001
button_to_click = Button.left
start_stop_key = KeyCode(char='a')
terminate_key = KeyCode(char='b')


class ClickMouse(threading.Thread):
    """
    class to create a mouse object for auto clicker

    :parameter:
    delay: the delay to set between mouse clicks

    button_to_click: the mouse button to be clicked

    self.running is initially set too false to avoid unwanted mouse clicks
    """

    def __init__(self, delay, button_to_click):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button_to_click = button_to_click
        self.running = False
        self.program_running = True

    # method to set the running flag to True
    def start_clicking(self):
        self.running = True

    # method to set the running flag to False
    def stop_clicking(self):
        self.running = False

    # exit method
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        """
        loop will run as long as program_running is true.
        checks to see if ClickMouse is running
        and clicks the button with the given delay.
        """
        while self.program_running:
            while self.running:
                mouse.click(self.button_to_click)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button_to_click)
click_thread.start()


def on_press(key):
    """
    on press takes any key as an input and checks it against
    the set start and stop keys.

    start_stop_key will stop clicking if running flag is True,
    will start clicking if running is currently False.
    """
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    # exit method called when full terminate key is pressed
    elif key == terminate_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
