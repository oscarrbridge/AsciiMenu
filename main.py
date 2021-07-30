import keyboard
import time
from ascii_menu import *


def change_screen(option):
    return ASCII_DICT[option]


if __name__ == "__main__":
    menu_option = 1

    print(change_screen(menu_option))

    while True:
        if keyboard.is_pressed("down") and menu_option < 7:
            if menu_option == 0:
                menu_option = 1
            menu_option += 1
            try:
                print(change_screen(menu_option))
                time.sleep(0.2)
            except ValueError:
                time.sleep(0.2)

        if keyboard.is_pressed("up") and menu_option >= 0:

            menu_option -= 1
            try:
                print(change_screen(menu_option))
                time.sleep(0.2)
            except KeyError:
                time.sleep(0.2)
