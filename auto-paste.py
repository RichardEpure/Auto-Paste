import win32clipboard
import keyboard


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
        if index < len(data):
            keyboard.send("tab")

def __main__():
    keyboard.add_hotkey("c+v", paste)
    keyboard.wait()


if __name__ == "__main__":
    print("Close this terminal to stop auto-paste")
    __main__()
