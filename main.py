import pyautogui
import time

# Configuração de segurança - pausa entre movimentos e para de executar se o mouse for para os cantos
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

def look_right_90deg():
  print("Olhar para a direita")
  pyautogui.moveRel(57, 0, duration=1) # 89.7deg
  pyautogui.moveRel(2, 0, duration=0.2)
  pyautogui.moveRel(-1, 0, duration=0.35)

def look_left_90deg():
  print("Olhar para a esquerda")
  pyautogui.moveRel(-57, 0, duration=1) # 89.7deg
  pyautogui.moveRel(-2, 0, duration=0.2)
  pyautogui.moveRel(1, 0, duration=0.35)

def look_back():
  print("Olhar para trás")
  pyautogui.moveRel(114, 0, duration=1)
  pyautogui.moveRel(1, 0, duration=0.2)

def reset_camera_position():
  pyautogui.press('t')
  time.sleep(0.2)
  # press "up" key
  pyautogui.press('up')
  time.sleep(0.2)
  pyautogui.press('enter')
  time.sleep(0.2)

# reset mouse to 100, 100
print("Movimento inicial")
pyautogui.moveTo(100, 100)


pyautogui.leftClick()
pyautogui.press('esc')

# wait 1 seconds
reset_camera_position()
time.sleep(0.3)

look_back()
time.sleep(0.5)

# 1 = 1.5deg

# testing
