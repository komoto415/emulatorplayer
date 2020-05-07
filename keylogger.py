from pynput.keyboard import Key, Listener
from datetime import datetime
import os


# We will only record these keys because they are the only ones that matter to the emulators
keys_whitelist = [
    'W', 'A', 'S', 'D', 'Z', 'X',
    "BACKSPACE", "ENTER", "SPACE",
]

# Character count just to know when to newline our text file just to help some readability. Might remove to simplify
# file reading of the emulator player if the newline character makes is more difficult
char_count = 0
now = datetime.isoformat(datetime.now())
now = now.replace('T', '-').replace(':', '-')[:-4]


def on_press(key):
    # Update the text file for each key pressed
    write_to_file(key)


# Escape key will kill the key logger script
def on_release(key):
    if key is Key.esc:
        return False


def write_to_file(key):
    global char_count, now

    with open(os.path.join("./logs", f"logger_{now}.txt"), "a") as f:
        trimmed_key = str(key).replace("'", "").upper()

        # Trimming the string of the special key cases
        if "KEY." in trimmed_key:
            trimmed_key = trimmed_key[4:]

        if trimmed_key in keys_whitelist:
            f.write(trimmed_key)
            char_count += len(trimmed_key)

            if char_count > 100 and char_count is not 0:
                f.write('\n')
                char_count = 0
            else:
                f.write(' ')
                char_count += 1


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
