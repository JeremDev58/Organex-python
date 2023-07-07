class Planner:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name")
        if kwargs.get("dynamic", False):
            pass
        self._tasks: list(object) = []

    def rename(self, value_str: str):
        self._set_name(value_str)

    def _set_name(self, value_str: str):
        self.name = value_str

    def add_task(self, task: object):
        self._tasks.append(task)

    def remove_task():
        pass