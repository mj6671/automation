import pyautogui as pag

position= pag.locateOnScreen('im not robot.png',confidence=0.8)
position2=pag.locateOnScreen('sumbit button.png',confidence=0.8)
pag.doubleClick(position)
pag.click(position2,duration=1)
