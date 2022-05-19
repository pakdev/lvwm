from __future__ import annotations

import argparse
from typing import Optional

from gui import WindowManagerApp


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


def main():
    WindowManagerApp().run()


if __name__ == "__main__":
    main(**vars(parse_args()))
