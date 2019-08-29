import pyautogui
import time
try:
	while True:
		pyautogui.moveTo(100, 100, duration=1)
		pyautogui.moveTo(786, 100, duration=1)
		pyautogui.click()
		time.sleep(240)
#		pyautogui.moveTo(278, 200, duration=0.25)
#		pyautogui.moveTo(189, 200, duration=0.25)
except KeyboardInterrupt:
	print('\nDone.')