import win32clipboard
import keyboard
import pystray
import PIL.Image


enabled = True
icon = None

def paste():
    global enabled

    if not enabled:
        return

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


def toggle_enabled():
    global enabled
    enabled = not enabled
    setup_context_menu()

def setup_context_menu():
    global enabled

    toggle_enabled_menu = pystray.MenuItem(f"Active: {enabled}", toggle_enabled)
    exit_menu = pystray.MenuItem("Exit", lambda: icon.stop())

    menu = pystray.Menu(
        toggle_enabled_menu,
        exit_menu
    )
    icon.menu = menu

def main():
    global icon

    keyboard.add_hotkey("c+v", paste)
    
    image = PIL.Image.open("./assets/icon.png")
    icon = pystray.Icon("Auto Paste", image, title="Auto Paste")
    setup_context_menu()
    icon.run()


if __name__ == "__main__":
    main()
