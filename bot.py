import pyautogui
import time
import win32api, win32con
import keyboard
import random

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# keyboard.is_pressed('q') !=
if __name__ == '__main__':
    while not keyboard.is_pressed('q'):
        print('in loop')
        pic = pyautogui.screenshot(region=(374, 268, 600, 420))
        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))
                if b in range(170, 210):
                    click(x + 374, y + 268)
                    time.sleep(0.05)
                    break
