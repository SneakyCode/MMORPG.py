import cv2, pyautogui, keyboard, sys
import numpy as np

imgs_to_find = [
    cv2.imread('rat1.png'),
    cv2.imread('rat2.png'),
    cv2.imread('rat3.png'),
    cv2.imread('rat.png')
]

prog_treshold = 0.8

while True:
	scr = pyautogui.screenshot()
	scr_cv = cv2.cvtColor(np.array(scr), cv2.COLOR_RGB2BGR)
	for img_to_find in imgs_to_find:
        if img_to_find is None:
            continue

        s_h, s_w = img_to_find.shape[:2]
		result = cv2.matchTemplate(scr_cv, img_to_find, cv2.TM_CCOEFF_NORMED)
		_, max_val, _, max_loc = cv2.minMaxLoc(result)
	
		if max_val >= prog_treshold:
			x, y = max_loc
			x2, y2 = x + s_w, y + s_h
			center = (max_loc[0] + s_w // 2, max_loc[1] + s_h // 2)
	
    	    pyautogui.click(center[0], center[1])
    	    pyautogui.sleep(10)
	
		if keyboard.is_pressed('q'):
			break

sys.exit()
