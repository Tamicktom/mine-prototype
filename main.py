import pyautogui
import time
import threading
from typing import Optional
from dotenv import load_dotenv
import os
from PIL import ImageGrab
import base64
import json

from openai import OpenAI

# load the .env file variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

def open_inventory():
  print("Abrir inventário")
  pyautogui.press('e')

def print_screenshot():
  # Capture the screenshot
  screenshot = ImageGrab.grab(bbox=(0, 30, 1280, 1030))
  
  # Save the screenshot to a file
  screenshot.save("screenshot.png")
  
  # Print the screenshot
  screenshot.close()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode("utf-8")

# reset mouse to 100, 100
print("Movimento inicial")
pyautogui.moveTo(100, 100)

swimming = SwimmingController()

pyautogui.leftClick()
pyautogui.press('esc')

# wait 1 seconds
reset_camera_position()
time.sleep(0.3)


# print_screenshot()

# base64_image = encode_image("screenshot.png")

# tools = [{
#   "type": "function",
#   "function": {
#     "name" : "look_right_90deg",
#     "description": "Look right 90 degrees",
#     "parameters": {}
#   }
# },{
#   "type": "function",
#   "function": {
#     "name" : "look_left_90deg",
#     "description": "Look left 90 degrees",
#     "parameters": {}
#   }
# },
# {
#   "type": "function",
#   "function" : {
#     "name": "open_inventory",
#     "description": "Open the inventory to see what you have",
#     "parameters": {}
#   }
# }
# ]

# messages = [
#   {
#     "role": "user",
#     "content": [
#       {
#         "type": "text",
#         "text": "You are playing Minecraft. Control and use the tools.",
#       },
#       {
#         "type": "image_url",
#         "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
#       },
#     ],
#   }
# ]

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=messages,
#     tools=tools,
# )

# def call_function(name, args):
#   if name == "look_right_90deg":
#       return look_right_90deg(**args)
#   if name == "look_left_90deg":
#       return look_left_90deg(**args)
#   if name == "open_inventory":
#       return open_inventory(**args)

# for tool_call in response.choices[0].message.tool_calls:
#   name = tool_call.function.name
#   args = json.loads(tool_call.function.arguments)

#   result = call_function(name, args)

# used_tools = []

# print(response.choices[0])
