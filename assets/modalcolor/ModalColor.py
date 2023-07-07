from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty

class ModalColor(ModalView):
    widget = ObjectProperty()
    def dismiss(self, *largs, **kwargs):
        self.widget.text = kwargs.get("color_title", "Rouge")
        self.widget.color = kwargs.get("color_choose", "#DA493D")
        return super().dismiss(*largs, **kwargs)