# this is part of the DYGtubeMobile project.
#
# Release: v1.0-dev1
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


import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pytube import YouTube
from pytube.cli import on_progress


class DYGTubeMobile(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Criar entrada de texto
        text_input = toga.TextInput(style=Pack(flex=1))


        # Criar botão
        button = toga.Button('Download MP3', on_press=self.button_handler, style=Pack(padding=10))

        # Box para centralizar os elementos
        center_box = toga.Box(style=Pack(direction=ROW, padding=20, alignment='center'))
        center_box.add(text_input)
        center_box.add(button)

        main_box.add(center_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_handler(self, widget):
        print("Texto digitado: ", widget.text)

        try:
            yt = YouTube(widget.text, on_progress_callback=on_progress)
            ys = yt.streams.get_audio_only()
            ys.download()
        except:
            pass



def main():
    return DYGTubeMobile()
