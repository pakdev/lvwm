from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

from layout import MonocleLayout


class WindowManager(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._layout = MonocleLayout()

        Window.bind(on_maximize=self._layout.on_mamimize)
        Window.bind(on_minimize=self._layout.on_minimize)
        Window.bind(on_restore=self._layout.on_restore)
        Window.bind(on_resize=self._layout.on_resize)


class WindowManagerApp(App):
    def build(self):
        return WindowManager()
