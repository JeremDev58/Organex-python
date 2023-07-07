"""from tkinter import Button
from turtle import title
import kivy

from assets.modaltime.ModalTime import ModalTime
kivy.require('2.0.0') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.effects.scroll import ScrollEffect
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import NumericProperty, BooleanProperty, ListProperty
import os
import re
from assets.modaltime.ModalTime import ModalTime
from kivy.utils import get_color_from_hex
from kivy.cache import Cache
Clock.max_iteration = 40


class MyApp(App):
    color_el = ["#2D322F", "#49514D"]
    color_font = ["#F1F3F2", "#CBCFCD"]
    font_size = ["20dp", "10sp"]
    color_primary = "#DA493D"
    kw_font_size = {'h1': '40dp', 'h2': '30dp', 'normal': '20dp', 'sub': '10dp'}

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.src_icons = os.path.join(os.getcwd(),"theme/icons/dark")
        self.master_wid = Builder.load_file("test.kv")

    def build(self):
        return self.master_wid

    def info(self):
        print(self.__dict__)
    

class BtnCheck(ButtonBehavior, BoxLayout):
    def on_press(self):
        print(self.ids)
        if self.ids.check.active:
            self.ids.check.active = False
        else:
            self.ids.check.active = True


class Btn(Button):
    def on_press(self):
        modal = ModalTime(widget=self)
        modal.open()



MyApp().run()"""
