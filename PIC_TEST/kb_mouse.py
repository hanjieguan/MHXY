from pynput import mouse
from PIL import ImageGrab
import time

mouse_controller = mouse.Controller()
mouse_button = mouse.Button
mouse_controller.position = (642, 268)
mouse_controller.press(mouse_button.left)
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    # im = ImageGrab.grab((x, y, x+20, y+20))
    # im.show()


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x-2, y)))

    if not pressed:
        # Stop listener
        return False
        # print('sss')
        # im = ImageGrab.grab((x, y, x + 60, y + 60))
        # tim = 'm' + str(int(time.time())) + '.png'
        # im.save(r'C:\Users\Administrator\Desktop\mh/' + tim)

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()