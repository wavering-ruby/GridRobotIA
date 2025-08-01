from ui.user_interface import UserInterface

if __name__ == "__main__":
    app = UserInterface()
    app.run()

# to create the executable: python -m PyInstaller --noconfirm --clean --windowed --add-data "assets;assets" --add-data "core;core" --add-data "ui;ui" main.py