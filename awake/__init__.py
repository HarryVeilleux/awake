import pyautogui
import time


__version__ = '1.0.1'


def awake(wtime: int = 150) -> None:
    """Alternates volumeup/volumedown key presses."""
    while True:
        pyautogui.press('volumeup')
        time.sleep(wtime)
        pyautogui.press('volumedown')
        time.sleep(wtime)
