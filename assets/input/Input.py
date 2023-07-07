from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.text import Label

class BaseInput(TextInput):
    max_c = NumericProperty(20)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.resize_text)

    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_c:
            substring = ''
        return super().insert_text(substring, from_undo)
    
    def resize_text(self, ev):
        self.size = self.get_text_size('M' * self.max_c)

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
