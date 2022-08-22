import pynput

board_controller = pynput.keyboard.Controller()
board_key = pynput.keyboard.Key
mouse_controller = pynput.mouse.Controller()
mouse_button = pynput.mouse.Button

# 634 268
# mouse_controller.position = (642, 268)
# mouse_controller.press(mouse_button.left)
# mouse_controller.position = (2, 0)
# mouse_controller.release(mouse_button.left)


# mouse_controller.position = (647, 268)
# mouse_controller.press(mouse_button.left)
# mouse_controller.position = (653, 0)
# mouse_controller.release(mouse_button.left)

# mouse_controller.position = (642, 268)
# mouse_controller.press(mouse_button.left)
# mouse_controller.position = (2, 517)
# mouse_controller.release(mouse_button.left)


mouse_controller.position = (642, 268)
mouse_controller.press(mouse_button.left)
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x-2, y)))

    if not pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

# Collect events until released
with pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = pynput.mouse.Listener(on_move=on_move, on_click=on_click)
listener.start()