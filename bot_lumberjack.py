import pyautogui
import time

galhos = [None, None, None, None, None, None]

time.sleep(2)
while True:
    time.sleep(0.278)
    # print(pyautogui.position())
    im = pyautogui.screenshot()
    # print(im.getpixel(pyautogui.position()))

    for i in range(6):
        # galhos[i] = im.getpixel((830, 640 - i * 100)) == (211, 247, 255)
        galhos[i] = im.getpixel((874, 671 - i * 100)) != (161, 116, 56)

    print(galhos)

    for i in range(6):
        if(galhos[i]):
            pyautogui.press('left')
            pyautogui.press('left')
        else:
            pyautogui.press('right')
            pyautogui.press('right')
