import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, W, A, S, D, Z, X, BACKSPACE, ENTER, SPACE


def convert_key_to_scan_code(key):
    ket_to_scan_code = {
        'W': W,
        'A': A,
        'S': S,
        'D': D,
        'Z': Z,
        'X': X,
        "BACKSPACE": BACKSPACE,
        "ENTER": ENTER,
        "SPACE": SPACE
    }
    return ket_to_scan_code.get(key, default=None)


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=150)
    return processed_img


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        PressKey(W)
        screen = np.array(ImageGrab.grab(bbox=(0, 65, 900, 665)))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
