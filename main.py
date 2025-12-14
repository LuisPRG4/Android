# main.py

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast


class ContentScreen(BoxLayout):
    file_menu = ObjectProperty(None)
    edit_menu = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_file_menu()
        self.create_edit_menu()
        self.load_note()

    # ---------- MENÚ ARCHIVO ----------
    def create_file_menu(self):
        menu_items = [
            {
                "text": "Nuevo",
                "icon": "file-plus",
                "on_release": lambda: self.new_note(),
            },
            {
                "text": "Guardar",
                "icon": "content-save",
                "on_release": lambda: self.save_note(),
            },
            {
                "text": "Salir",
                "icon": "exit-to-app",
                "on_release": lambda: MDApp.get_running_app().stop(),
            },
        ]

        self.file_menu = MDDropdownMenu(
            caller=self.ids.toolbar_file_button,
            items=menu_items,
            width_mult=4,
        )

    # ---------- MENÚ EDITAR ----------
    def create_edit_menu(self):
        menu_items = [
            {
                "text": "Copiar",
                "icon": "content-copy",
                "on_release": lambda: self.copy_text(),
            },
            {
                "text": "Pegar",
                "icon": "content-paste",
                "on_release": lambda: self.paste_text(),
            },
        ]

        self.edit_menu = MDDropdownMenu(
            caller=self.ids.toolbar_edit_button,
            items=menu_items,
            width_mult=4,
        )

    def show_file_menu(self):
        self.file_menu.open()

    def show_edit_menu(self):
        self.edit_menu.open()

    # ---------- NOTAS ----------
    def new_note(self):
        self.ids.text_field.text = ""
        self.update_status("Nueva nota creada")
        self.file_menu.dismiss()

    def save_note(self):
        try:
            with open(self.get_file_path(), "w", encoding="utf-8") as f:
                f.write(self.ids.text_field.text)
            self.update_status("Nota guardada con éxito")
            toast("¡Nota guardada!")
        except Exception as e:
            self.update_status(f"Error al guardar: {e}")
            toast("Error al guardar")
        finally:
            self.file_menu.dismiss()

    def load_note(self):
        try:
            path = self.get_file_path()
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    self.ids.text_field.text = f.read()
                self.update_status("Nota cargada")
        except Exception as e:
            self.update_status(f"Error al cargar: {e}")

    # ---------- PORTAPAPELES ----------
    def copy_text(self):
        self.ids.text_field.copy()
        toast("Texto copiado")
        self.edit_menu.dismiss()

    def paste_text(self):
        self.ids.text_field.paste()
        toast("Texto pegado")
        self.edit_menu.dismiss()

    # ---------- ARCHIVO ----------
    def get_file_path(self):
        if platform == "android":
            return os.path.join(
                App.get_running_app().user_data_dir,
                "nota.txt"
            )
        return "nota.txt"

    # ---------- UI ----------
    def update_status(self, message):
        self.ids.status_bar.text = message


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        return ContentScreen()

    def minimize_window(self):
        toast("Función de minimizar (próximamente)")


if __name__ == "__main__":
    MainApp().run()
