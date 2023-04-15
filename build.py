import subprocess
import shutil
import os


icon_path = "assets/icon.png"
build_path = "dist/auto-paste"

subprocess.run(["pyinstaller", f"--icon=./{icon_path}", "--noconsole", "auto-paste.py"], shell=True)
os.makedirs(f"{build_path}/assets", exist_ok=True)
shutil.copy2(icon_path, f"{build_path}/{icon_path}")
shutil.make_archive(build_path, "zip", build_path)
