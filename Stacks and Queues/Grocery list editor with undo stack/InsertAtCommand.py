from Stack import Stack
from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, source, index, new_item):
        # Type your code here.
        # insert new_item at index in source
        self.source_list = source
        self.index = index
        self.new_item = new_item
        self.executed = False
        self.previous_values = (None, None)

    def execute(self):
        # Type your code here.
        # insert new_item at index in source_list
        self.source_list.insert(self.index, self.new_item)
        self.executed = True
        return True
    def undo(self):
        # Type your code here.
        # remove the item at index in source_list
        if self.executed:
            del self.source_list[self.index]
            self.executed = False
            return True
        return False
