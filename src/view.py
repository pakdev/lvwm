from __future__ import annotations

import ahkpy


class VirtualInstrument:
    pass


class Project:
    def get_vis(self) -> list[VirtualInstrument]:
        pass


class LabViewManager:
    def get_projects(self) -> list[Project]:
        pass
