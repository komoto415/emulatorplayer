import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, W, A, S, D, Z, X, BACKSPACE, ENTER, SPACE
import os

DEVICE = "GBA"

def convert_key_to_scan_code(key):
    key_to_scan_code = get_conversion_dict()
    return key_to_scan_code.get(key)

def get_conversion_dict():
    emulator = {
        "GBA": {
            'W': W,
            'A': A,
            'S': S,
            'D': D,
            'Z': Z,
            'X': X,
            "BACKSPACE": BACKSPACE,
            "ENTER": ENTER,
            "SPACE": SPACE
        },
        "DS": {

        },
    }
    return emulator.get(DEVICE)

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=150)
    return processed_img

def main():
    running = False
    print("Starting runner in", end="")
    for i in reversed(list(range(5))):
        print(f" {i + 1}...", end="")
        time.sleep(1)
    file = "TestKeys.txt"
    if os.path.exists(file):
        while True:
            screen = np.array(ImageGrab.grab(bbox=(0, 65, 900, 665)))
            last_time = time.time()
            new_screen = process_img(screen)
            cv2.imshow('window', new_screen)
            # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
            if not running:
                running = True
                with open(file, "r") as f:
                    for line in f.readlines()[:-1]:
                        time.sleep(0.5)
                        key = line.strip()
                        PressKey(convert_key_to_scan_code(key))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    else:
        print("Either your file doesn't exist, is named incorrectly or is in another castle")

if __name__ == '__main__':
    main()
