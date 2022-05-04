import pyautogui
import time

def awake(wtime: int = 150) -> None:
    """Alternate volumeup/volumedown key presses."""
    while True:
        pyautogui.press('volumeup')
        time.sleep(wtime)
        pyautogui.press('volumedown')
        time.sleep(wtime)
