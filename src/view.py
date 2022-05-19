from __future__ import annotations

from abc import ABC
import re

import ahkpy


class View(ABC):
    pass


class VirtualInstrument(View):
    pass


class Project(View):
    def __init__(self, window):
        self._window = window
        match = re.search("(.+?) - Project Explorer", window.title)
        if match:
            print(match.groups[1])
            self._name = window.title

    def get_views(self) -> list[View]:
        pass


class LabViewManager:
    def get_projects(self) -> list[Project]:
        return [
            Project(win)
            for win in ahkpy.windows.filter(class_name="LVDChild")
            if "Project Explorer" in win.title
        ]
