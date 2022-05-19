from __future__ import annotations

from abc import ABC
from typing import cast

from kivy.core.window import Window

from view import LabViewManager, View


class Layout(ABC):
    def __init__(self) -> None:
        super().__init__()

        self._lv_manager = LabViewManager()
        projects = self._lv_manager.get_projects()

        self._views: list[View] = cast(list[View], projects)
        self._visible_views: list[View] = []

    def on_mamimize(self, window: Window):
        pass

    def on_minimize(self, window: Window, *args):
        pass

    def on_restore(self, window: Window, *args):
        pass

    def on_resize(self, window: Window, width: int, height: int):
        pass


class MonocleLayout(Layout):
    pass
