# this is part of the DYGtubeMobileApp project.
#
# Release: v1.0-dev3
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez



import time
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pytube import YouTube
from pytube.cli import on_progress


class HomeScreen(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        intro_label = toga.Label(
            'Welcome to GeoApp!',
            style=Pack(padding_bottom=20)
        )

        name_input = toga.TextInput(
            placeholder='Enter your name here...',
            style=Pack(flex=1, padding_bottom=10)
        )

        location_input = toga.TextInput(
            placeholder='Enter your location here...',
            style=Pack(flex=1, padding_bottom=10)
        )

        submit_button = toga.Button(
            'Submit',
            on_press=self.submit_form,
            style=Pack(padding=10)
        )

        main_box.add(intro_label)
        main_box.add(toga.Label('Name:', style=Pack(padding_bottom=5)))
        main_box.add(name_input)
        main_box.add(toga.Label('Location:', style=Pack(padding_bottom=5)))
        main_box.add(location_input)
        main_box.add(submit_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def submit_form(self, widget):
        """
        Function to handle form submission.
        """
        name = widget.window.content[1].value
        location = widget.window.content[3].value

        toga.dialog.info(
            'Form Submitted!',
            f'Thank you {name} from {location}!'
        )

def main():
    return HomeScreen()
