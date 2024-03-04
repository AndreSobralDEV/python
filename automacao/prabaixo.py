import pyautogui
import time

# Função para pressionar a tecla "Para baixo"
def press_down_key():
    pyautogui.press('down')

# Loop para pressionar a tecla a cada 15 segundos, repetidamente
try:
    while True:
        press_down_key()  # Pressiona a tecla "Para baixo"
        time.sleep(15)    # Aguarda 15 segundos
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")