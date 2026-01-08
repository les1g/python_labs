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
        # remove at given index from list_items
        self.list_items.pop(removal_index)

        # create an InsertAtCommand to undo the removal
        self.undo_stack.push(InsertAtCommand(self.list_items, removal_index, self.list_items[removal_index]))

    def swap_with_undo(self, index1, index2):
        # swap the items at index1 and index2 in list_items
        self.list_items[index1], self.list_items[index2] = self.list_items[index2], self.list_items[index1]
        # create a SwapCommand to undo the swap
        self.undo_stack.push(SwapCommand(self.list_items, index1, index2))

    def execute_undo(self):
        # call execute on the top command in the undo stack
        if self.undo_stack.size() > 0:
            undo_command = self.undo_stack.pop()
            undo_command.execute()

    def get_list_size(self):
       return len(self.list_items)

    def get_undo_stack_size(self):
       return self.undo_stack.size()

    def get_list_copy(self):
       return self.list_items[:]

    def print_list(self, outfil):
        for n, item in enumerate(self.list_items):
            print(f"""{n}. {item}""", file=outfil)
