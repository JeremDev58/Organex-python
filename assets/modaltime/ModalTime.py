from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty

class ModalTime(ModalView):
    widget = ObjectProperty()
    def dismiss(self, *largs, **kwargs):
        hour = self.ids.view_modal.content_modal.time.container.hour.input.text
        if hour == "":
            hour = self.ids.view_modal.content_modal.time.container.hour.input.hint_text
        if len(hour) == 1:
            hour+='0'
        minute = self.ids.view_modal.content_modal.time.container.minute.input.text
        if minute == "":
            minute = self.ids.view_modal.content_modal.time.container.minute.input.hint_text
        if len(minute) == 1:
            minute+='0'
        self.widget.text = hour + ':' + minute
        return super().dismiss(*largs, **kwargs)