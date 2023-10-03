from typing import Any


class Action:
    def __init__(self, name: str, description: str, action: function):
        self.name = name
        self.description = description
        self.act = action
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            return self.action(*args, **kwds)
        except Exception as e:
            print("Error in action: " + str(e))
            if input("Proceed?[y/N]") in "YESyes":
                return None
            exit(1)

    def __str__(self):
        return self.name + " - " + self.description

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.action == other.action

    def __hash__(self):
        return hash((self.name, self.description, self.action))

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name