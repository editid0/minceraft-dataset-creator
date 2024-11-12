from datetime import datetime, timezone
import pynput, win32gui
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

control_key_map = {
    '\x03': 'ctrl+c',
    '\x16': 'ctrl+v',
    '\x18': 'ctrl+x',
    '\x1a': 'ctrl+z',
    '\x17': 'ctrl+w',
}
to_exit = False
full_exit = False

# Track the last mouse position
last_mouse_position = None

def log_event(event_type, event_info):
    """Helper function to log events to a file."""
    if win32gui.GetWindowText (win32gui.GetForegroundWindow()) != "Minecraft* 1.21 - Singleplayer":
        return
    with open('log.txt', 'a') as f:
        timestamp = datetime.now(tz=timezone.utc).strftime("%H:%M:%S:%f")
        f.write(f"{timestamp} - {event_info} - {event_type}\n")
    print(f"{timestamp} - {event_info} - {event_type}")

# Keyboard event handlers
def on_key_press(key):
    global to_exit, full_exit
    if full_exit:
        exit(0)
    char = ''
    try:
        char = key.char
    except AttributeError:
        char = key.name
    if char in control_key_map:
        char = control_key_map[char]
    if char == 'ctrl_l':
        char = 'ctrl'
    if char == 'ctrl+z':
        full_exit = True
    log_event("key press", char)

    # Check for exit condition
    if key == Key.esc:
        to_exit = True
    if to_exit and key == Key.enter:
        exit(0)
    if to_exit and key == Key.space:
        to_exit = False

def on_key_release(key):
    global to_exit, full_exit
    if full_exit:
        exit(0)
    char = ''
    try:
        char = key.char
    except AttributeError:
        char = key.name
    if char in control_key_map:
        char = control_key_map[char]
    if char == 'ctrl_l':
        char = 'ctrl'
    log_event("key release", char)
    if char == 'ctrl+z':
        full_exit = True
    # Check for exit condition
    if key == Key.esc:
        to_exit = True
    if to_exit and key == Key.enter:
        exit(0)
    if to_exit and key == Key.space:
        to_exit = False

# Mouse event handlers
def on_click(x, y, button, pressed):
    global full_exit
    if full_exit:
        exit(0)
    action = "mouse press" if pressed else "mouse release"
    log_event(action, f"{button} at ({x}, {y})")

def on_scroll(x, y, dx, dy):
    global full_exit
    if full_exit:
        exit(0)
    log_event("mouse scroll", f"at ({x}, {y}) with delta ({dx}, {dy})")

def on_move(x, y):
    global last_mouse_position, full_exit
    if full_exit:
        exit(0)
    if last_mouse_position is not None:
        dx = x - last_mouse_position[0]
        dy = y - last_mouse_position[1]
        if dx != 0 or dy != 0:
            log_event("relative mouse move", f"delta ({dx}, {dy})")
    last_mouse_position = (x, y)

# Starting both keyboard and mouse listeners
with KeyboardListener(on_press=on_key_press, on_release=on_key_release) as k_listener, \
     MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move) as m_listener:
    k_listener.join()
    m_listener.join()
