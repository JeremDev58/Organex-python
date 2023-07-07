from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.core.text import Label
from kivy.uix.anchorlayout import AnchorLayout
import re
COLOR_FONT = ["#F1F3F2", "#CBCFCD"]
COLOR_PRIMARY = "#DA493D"

class InputNum(TextInput):
    max_c = NumericProperty(2)
    is_hour = BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.resize_text)
        self.bind(focus=self.on_focus)
        self.zero_to_two = re.compile('[^0-2]')
        self.zero_to_three = re.compile('[^0-3]')
        self.zero_to_five = re.compile('[^0-5]')
        self.num = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_c:
            substring = ''
        else:
            if self.is_hour:
                if not len(self.text):
                    substring = re.sub(self.zero_to_two, '', substring)
                elif self.text[0] == '2':
                    substring = re.sub(self.zero_to_three, '', substring)
            else:
                if not len(self.text):
                    substring = re.sub(self.zero_to_five, '', substring) 
        return super().insert_text(substring, from_undo)
    
    def resize_text(self, ev):
        self.size = self.get_text_size(self, self.hint_text)

    @staticmethod
    def get_text_size(self, text):
        try:
            kw = self._get_line_options()
            text = text.replace('\t', ' ' * self.tab_width)
        except:
            kw = {
                'font_size': self.font_size,
                'font_name': self.font_name,
                'font_context': self.font_context,
                'font_family': self.font_family,
                'text_language': self.text_language,
                'base_direction': self.base_direction,
                'anchor_x': 'left',
                'anchor_y': 'top',
                'padding_x': 0,
                'padding_y': 0,
                'padding': (0, 0)
            }
        return Label(**kw).get_extents(text)

    def on_focus(self, ev, is_focus):
        if is_focus:
            self.parent.line.canvas.get_group('color')[0].rgba = get_color_from_hex(COLOR_PRIMARY)
        else:
            self.parent.line.canvas.get_group('color')[0].rgba = get_color_from_hex(COLOR_FONT[1])


class InputTime(AnchorLayout):
    margin_x = ListProperty([0, 0])
    margin_y = ListProperty([0, 0])
    margin = ListProperty([0, 0, 0, 0])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.margin_x = [0.1*self.width, 0.1*self.width]
        self.margin_y = [0.1*self.height, 0.1*self.height]