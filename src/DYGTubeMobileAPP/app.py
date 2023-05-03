# this is part of the DYGtubeMobileApp project.
#
# Release: v1.0-dev2
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
        self.main_window = toga.MainWindow(title=self.formal_name)


        button1 = toga.Button('Tela 1', on_press=self.show_screen1, style=Pack(padding=10))

        button2 = toga.Button('Tela 2', on_press=self.show_screen2, style=Pack(padding=10))

        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        main_box.add(button1)
        main_box.add(button2)

        self.main_window.content = main_box


        self.main_window.show()

    def show_screen1(self, widget):

        screen1 = Screen1()

        self.main_window.content = screen1

    def show_screen2(self, widget):

        screen2 = Screen2()

        self.main_window.content = screen2


class Screen1(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, padding=10))

        
        button = toga.Button('Voltar', on_press=self.show_home_screen, style=Pack(padding=10))

       
        self.add(button)

    def show_home_screen(self, widget):
       
        HomeScreen()


class Screen2(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, padding=10))

        button = toga.Button('Voltar', on_press=self.show_home_screen, style=Pack(padding=10))

        self.add(button)

    def show_home_screen(self, widget):
   
        home_screen = HomeScreen()
   
        widget.app.main_window.content = home_screen


def main():
    return HomeScreen()
