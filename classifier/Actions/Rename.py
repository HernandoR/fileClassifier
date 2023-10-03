from typing import Any
from Actions.Action import Action

class Rename(Action):
    def __init__(self):
        super().__init__("Rename", "Renames a file", self.rename)
    
    def rename(self, file, new_name):
        file.rename(new_name)
        return file
