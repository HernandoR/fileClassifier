from typing import Any
import Action
from pathlib import Path
import os
class Rename(Action):
    def __init__(self):
        super().__init__("Rename", "Renames a file", self.rename)
    
    def rename(self, file: str|Path, new_name: str):
        src=Path(file)
        des=src.parent/new_name
        src.rename(des)
        
            
