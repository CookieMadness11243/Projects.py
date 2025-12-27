import pyautogui

for i in range(100):
    try:
        pyautogui.locateCenterOnScreen("O.png", confidence=0.8, grayscale=True)
    except:
        x, y = pyautogui.locateCenterOnScreen("LB.png", confidence=0.8, grayscale=True)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    else:
        x, y = pyautogui.locateCenterOnScreen("OB.png", confidence=0.8, grayscale=True)
        pyautogui.moveTo(x, y)
        pyautogui.click()

#pyautogui.displayMousePosition()