import pyautogui
import time
import keyboard

running = True

def click_loop():
    while running:
        x, y = pyautogui.position()  # Obtenir les coordonnées actuelles de la souris
        pyautogui.click(x, y)  # Cliquer à l'emplacement de la souris
        time.sleep(0.0001)  # Attendre 0.0001 seconde entre chaque clic

# Lancer la boucle de clic dans un thread
click_thread = threading.Thread(target=click_loop)
click_thread.start()

# Fonction pour arrêter le script en appuyant sur F6
def stop_script():
    global running
    running = False

keyboard.add_hotkey('f6', stop_script)

# Attendre que la boucle de clic se termine
click_thread.join()
