import pynput

board_controller = pynput.keyboard.Controller()
board_key = pynput.keyboard.Key
mouse_controller = pynput.mouse.Controller()
mouse_button = pynput.mouse.Button

# 634 268
mouse_controller.position = (642, 268)
mouse_controller.press(mouse_button.left)
mouse_controller.position = (2, 0)
mouse_controller.release(mouse_button.left)

# 635 268
# mouse_controller.position = (955,290)
# mouse_controller.press(mouse_button.right)
# mouse_controller.release(mouse_button.right)
# mouse_controller.position = (556, 268)
# mouse_controller.press(mouse_button.left)
# mouse_controller.position = (2, 517)
# mouse_controller.release(mouse_button.left)
