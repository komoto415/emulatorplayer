from pynput.keyboard import Key, Listener
from datetime import datetime
import os

# Logistics sake for file naming
NOW = datetime.isoformat(datetime.now())
NOW = NOW.replace('T', '-').replace(':', '-')[:-4]

# What device we will be whitelisting keys for
DEVICE = "GBA"

# We will only record these keys because they are the only ones that matter to the emulators
# For some scalability if we decided to branch out to other games, we'll just have a simple getter for the list of keys
# that will be whitelisted based on the keymap configuration for any particular device, as determined by our DEVICE
# constant
def get_key_whitelist():
    whitelist = {
        "GBA": [
            'W', 'A', 'S', 'D', 'Z', 'X',
            "BACKSPACE", "ENTER", "SPACE",
        ],
        "DS": [

        ],
    }
    return whitelist.get(DEVICE)

def on_press(key):
    # Update the text file for each key pressed
    write_to_file(key)

# Escape key will kill the key logger script
def on_release(key):
    if key is Key.esc:
        return False

def write_to_file(key):
    with open(os.path.join("./logs", f"logger_{NOW}.txt"), "a") as f:
        trimmed_key = str(key).replace("'", "").upper()

        # Trimming the string of the special key cases
        if "KEY." in trimmed_key:
            trimmed_key = trimmed_key[4:]

        if trimmed_key in get_key_whitelist():
            # For the sake ease when using Python's native readlines function, either each line is the key pressed or
            # have it all recorded in one line separated by spaces. Doesn't matter which one, just picked on arbitrarily
            f.write(trimmed_key)
            f.write('\n')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
