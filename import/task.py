import enum

class StateTask(enum.Enum):
	Wait = 0
	Run = 1
	End = 2

class Task:
	def __init__(self, **kwargs):
		self.name = kwargs.get("name")
		self.trigger = kwargs.get("trigger")
		self.end = kwargs.get("end")
		self.state = StateTask.Wait
		
	def rename(self, name):
		self.name = name
		
	def signal_start():
		pass
	
	def signal_end():
		pass
		
	def start():
		pass
	
	def end():
		pass