from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior

class BtnCheck(ButtonBehavior, BoxLayout):
    def on_press(self):
        print(self.ids)
        if self.ids.check.active:
            self.ids.check.active = False
        else:
            self.ids.check.active = True