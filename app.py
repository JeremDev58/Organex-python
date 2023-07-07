from kivy.app import App
from kivy.lang import Builder
import time
from conf import Configure

class Organex(App):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.handler = Configure()
		self.tasks = []
		self.planners = []
		self.events = []
		
		self.master_widget = Builder.load_file("main.kv")
			
	def build(self):
		return self.master_widget
	
	def get_date(self):
		return time.strftime("%a, %d %b")
