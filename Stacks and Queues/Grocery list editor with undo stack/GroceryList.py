from Stack import Stack
from InsertAtCommand import InsertAtCommand
from RemoveLastCommand import RemoveLastCommand
from SwapCommand import SwapCommand

class GroceryList:
    def __init__(self):
        self.list_items = []
        self.undo_stack = Stack()

    def add_with_undo(self, new_item_name):
        # Add the list item
        self.list_items.append(new_item_name)

        # Make an undo command that removes the last item and pushes it onto the undo stack
        self.undo_stack.push(RemoveLastCommand(self.list_items))

    def remove_at_with_undo(self, removal_index):
        # Type your code here.
        pass

    def swap_with_undo(self, index1, index2):
        # Type your code here.
        pass

    def execute_undo(self):
        # Type your code here.
        pass

    def get_list_size(self):
       return len(self.list_items)

    def get_undo_stack_size(self):
       return self.undo_stack.size()

    def get_list_copy(self):
       return self.list_items[:]

    def print_list(self, outfil):
        for n, item in enumerate(self.list_items):
            print(f"""{n}. {item}""", file=outfil)
