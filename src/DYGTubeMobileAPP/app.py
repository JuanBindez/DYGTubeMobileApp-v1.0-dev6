# this is part of the DYGtubeMobileApp project.
#
# Release: v1.0-dev5
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

from pytube import YouTube
from pytube.cli import on_progress

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

import os


class HomeScreen(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # adiciona o campo de texto
        self.text_input = toga.TextInput(style=Pack(flex=1, padding_bottom=10))
        main_box.add(self.text_input)

        # adiciona o botão que imprime o texto
        submit_button = toga.Button(
            'Dowload MP3',
            on_press=self.submit_form,
            style=Pack(padding=10)
        )
        main_box.add(submit_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def submit_form(self, widget):
        """
        Function to handle form submission.
        """
        text = self.text_input.value
        print(text)

        yt = YouTube(text, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()

        # Obtém o caminho absoluto do diretório de downloads do dispositivo Android
        download_dir = os.path.join(os.path.expanduser('~'), 'Download')

        # Baixa o arquivo no diretório de downloads do dispositivo Android
        ys.download(download_dir)


def main():
    return HomeScreen()
