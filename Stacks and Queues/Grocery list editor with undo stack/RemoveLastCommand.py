from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, source):
        super().__init__()
        self.source_list = source

    def execute(self):
        # Type your code here.
        self.removed_item = self.source_list.pop()
    def undo(self):
        # Type your code here.
        self.source_list.append(self.removed_item)
        return True
