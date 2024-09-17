#!/usr/bin/python3
import shutil
import subprocess
import urllib.parse

from gi import require_version

require_version("Nautilus", "4.0")
require_version("Gtk", "4.0")

TERMINAL_NAME = "com.raggesilver.BlackBox"

import logging
import os
from gettext import gettext

from gi.repository import GObject, Nautilus

if os.environ.get("NAUTILUS_PTYXIS_DEBUG", "False") == "True": #what does this do?
    logging.basicConfig(level=logging.DEBUG)


class BlackBoxNautilus(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self.is_select = False
        pass

    def get_file_items(self, files: list[Nautilus.FileInfo]):
        """Return to menu when click on any file/folder"""
        if not self.only_one_file_info(files):
            return []

        menu = []
        fileInfo = files[0]
        self.is_select = False

        if fileInfo.is_directory():
            self.is_select = True
            dir_path = self.get_abs_path(fileInfo)

            logging.debug("Selecting a directory!!")
            logging.debug(f"Create a menu item for entry {dir_path}")
            menu_item = self._create_nautilus_item(dir_path)
            menu.append(menu_item)

        return menu

    def get_background_items(self, directory):
        """Returns the menu items to display when no file/folder is selected
        (i.e. when right-clicking the background)."""
        # Some concurrency problem fix.
        # when you select a directory, and right mouse, nautilus will call this
        # once the moments you focus the menu. This code to ignore that time.
        if self.is_select:
            self.is_select = False
            return []

        menu = []
        if directory.is_directory():
            dir_path = self.get_abs_path(directory)

            logging.debug("Nothing is selected. Launch from backgrounds!!")
            logging.debug(f"Create a menu item for entry {dir_path}")
            menu_item = self._create_nautilus_item(dir_path)
            menu.append(menu_item)

        return menu

    def _create_nautilus_item(self, dir_path: str) -> Nautilus.MenuItem:
        """Creates the 'Open In BlackBox' menu item."""

        item = Nautilus.MenuItem(
            name="BlackboxNautilus::open_in_blackbox",
            label=gettext("Open in BlackBox"),
            tip=gettext("Open this folder/file in BlackBox Terminal"),
        )
        logging.debug(f"Created item with path {dir_path}")

        item.connect("activate", self._nautilus_run, dir_path)
        logging.debug("Connect trigger to menu item")

        return item

    def is_native(self):
        if shutil.which("blackbox-terminal") == "/usr/bin/blackbox-terminal":
            return "blackbox-terminal"
        if shutil.which("blackbox") == "/usr/bin/blackbox":
            return "blackbox"

    def _nautilus_run(self, menu, path):
        """'Open with Ptyxis's menu item callback.""" #not sure what this does
        logging.debug("Openning:", path)
        args = None
        if self.is_native()=="blackbox-terminal":
            args = ["blackbox-terminal","-w", path]
        elif self.is_native()=="blackbox":
            args = ["blackbox","-w", path]
        else:
            args = ["/usr/bin/flatpak", "run", TERMINAL_NAME,"-w", path]

        subprocess.Popen(args, cwd=path)

    def get_abs_path(self, fileInfo: Nautilus.FileInfo):
        path = fileInfo.get_location().get_path()
        return path

    def only_one_file_info(self, files: list[Nautilus.FileInfo]):
        return len(files) == 1
