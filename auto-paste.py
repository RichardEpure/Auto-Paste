import win32clipboard
import keyboard
import pystray
import PIL.Image


def paste():
    try:
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except TypeError:
        clipboard = ""

    data = clipboard.split()
    keyboard.send("ctrl+a, delete")

    for index, item in enumerate(data):
        keyboard.write(item)
        if index < len(data)-1:
            keyboard.send("tab")

def main():
    keyboard.add_hotkey("c+v", paste)
    
    image = PIL.Image.open("./assets/icon.png")

    exit_menu = pystray.MenuItem("Exit", lambda: icon.stop())

    menu = pystray.Menu(
        exit_menu
    )

    icon = pystray.Icon("Auto Paste", image, menu=menu, title="Auto Paste")
    icon.run()


if __name__ == "__main__":
    main()
