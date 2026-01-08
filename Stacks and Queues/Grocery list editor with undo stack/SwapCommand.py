from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, source, index1, index2):
        # Type your code here.
        # source is the list where we will swap items at index1 and index2
        self.source_list = source
        self.index1 = index1
        self.index2 = index2
        self.executed = False
        self.previous_values = (None, None)

    def execute(self):
        # Type your code here.
        # swap the items at index1 and index2 in source_list
        if not self.executed:
            self.previous_values = (self.source_list[self.index1], self.source_list[self.index2])
            self.executed = True
        self.source_list[self.index1], self.source_list[self.index2] = self.source_list[self.index2], self.source_list[self.index1]
        
