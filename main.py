import pyautogui
import time
import threading
from typing import Optional

# Configuração de segurança - pausa entre movimentos e para de executar se o mouse for para os cantos
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

def look_right_90deg():
  print("Olhar para a direita")
  pyautogui.moveRel(57, 0, duration=1) # 89.7deg
  pyautogui.moveRel(2, 0, duration=0.2)
  pyautogui.moveRel(-1, 0, duration=0.35)
  
def look_right_45deg():
  print("Olhar um pouco para a direita")
  pyautogui.moveRel(107, 0, duration=0.25)

def look_left_90deg():
  print("Olhar para a esquerda")
  pyautogui.moveRel(-57, 0, duration=1) # 89.7deg
  pyautogui.moveRel(-2, 0, duration=0.2)
  pyautogui.moveRel(1, 0, duration=0.35)

def look_left_45deg():
  print("Olhar um pouco para a direita")
  pyautogui.moveRel(-107, 0, duration=0.25)

def look_down_45deg():
  print("Olhar um pouco para baixo")
  pyautogui.moveRel(0, 107, duration=0.25)

def look_up_45deg():
  print("Olhar um pouco para cima")
  pyautogui.moveRel(0, -107, duration=0.25)

def look_back():
  print("Olhar para trás")
  pyautogui.moveRel(114, 0, duration=1)
  pyautogui.moveRel(1, 0, duration=0.2)

def walk_forward(hold_time=1):
  print("Andar para frente")
  pyautogui.keyDown('w')
  time.sleep(hold_time)
  pyautogui.keyUp('w')

def walk_backward(hold_time=1):
  print("Andar para trás")
  pyautogui.keyDown('s')
  time.sleep(hold_time)
  pyautogui.keyUp('s')

def walk_left(hold_time=1):
  print("Andar para a esquerda")
  pyautogui.keyDown('a')
  time.sleep(hold_time)
  pyautogui.keyUp('a')

def walk_right(hold_time=1):
  print("Andar para a direita")
  pyautogui.keyDown('d')
  time.sleep(hold_time)
  pyautogui.keyUp('d')

def keep_swimming():
  print("Manter nadando")
  pyautogui.keyDown('space')

def reset_camera_position():
  pyautogui.press('t')
  time.sleep(0.2)
  # press "up" key
  pyautogui.press('up')
  time.sleep(0.2)
  pyautogui.press('enter')
  time.sleep(0.2)

class SwimmingController:
  def __init__(self):
    self.is_swimming = False
    self.swimming_thread: Optional[threading.Thread] = None
  
  def _swimming_loop(self):
    while self.is_swimming:
        pyautogui.keyDown('space')
        time.sleep(5)
        pyautogui.keyUp('space')
        time.sleep(0.1)
  
  def start_swimming(self):
    """Inicia o nado em segundo plano"""
    if not self.is_swimming:
        self.is_swimming = True
        self.swimming_thread = threading.Thread(target=self._swimming_loop)
        self.swimming_thread.start()
        print("Começou a nadar")
  
  def stop_swimming(self):
    """Para o nado"""
    if self.is_swimming:
        self.is_swimming = False
        if self.swimming_thread:
            self.swimming_thread.join()
        print("Parou de nadar")

def attack():
  print("Atacar")
  pyautogui.leftClick()

def place_or_use():
  print("Colocar ou usar")
  pyautogui.rightClick()

def clone_block():
  print("Clonar bloco")
  pyautogui.click(button="middle")

# reset mouse to 100, 100
print("Movimento inicial")
pyautogui.moveTo(100, 100)

swimming = SwimmingController()

pyautogui.leftClick()
pyautogui.press('esc')

# wait 1 seconds
reset_camera_position()
time.sleep(0.3)

look_down_45deg()
clone_block()
place_or_use()
walk_right(0.125)
place_or_use()
look_right_45deg()
look_up_45deg()

# 1 = 1.5deg

# testing
