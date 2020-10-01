"""  EPR1 - Übungsblatt 9 - Selection Sort
A GUI implementation of visualizing the selection sort algorithm using Tkinter.

Note: implementation is not complete. Only the result of the sorted list
will be displayed, but not the sorting algorithm itself.
"""

import tkinter as tk
from tkinter import messagebox
from time import sleep


#_____________________________________________________________________________

class SelectionSortAlg:

    def __init__(self):
        pass
    
    def sorting_alg(self, my_list):
        """ This Function takes a list of numbers and sorts them. 
        """
        for i in range(len(my_list)):
            min = i
            for j in range(i+1, len(my_list)):
                if my_list[min] > my_list[j]:
                    min = j
            my_list[i],my_list[min] = my_list[min],my_list[i]
        return my_list


class SelectionSortUI:

    def __init__(self, parent):

        self.sorting = SelectionSortAlg()

        self.window = parent
        self.window.title("Selection Sort")
        self.my_list = []
        self.my_unsorted_list_label_text = self.set_my_unsorted_list_label()
        self.my_sorted_list_label_text = self.set_my_sorted_list_label()

        # Define labels
        self.label_0 = tk.Label(self.window, 
                                text="Enter your numbers (integers)"+ 
                                     "- one by one: ")
        self.label_1 = tk.Label(self.window, 
                                text=self.my_unsorted_list_label_text)
        self.label_2 = tk.Label(self.window, 
                                text="Sorted list: " + str(self.my_list))

        # Place labels
        self.label_0.grid(row=0)
        self.label_1.grid(row=3, columnspan=3)
        self.label_2.grid(row=6, columnspan=3)

        # Define buttons
        self.add_to_list_button = tk.Button(self.window, 
                                    text="Add to list", 
                                    fg="black",
                                    width=50, 
                                    command=self.click_add_to_list_button)
        self.start_timed_sorting = tk.Button(self.window, 
                                    text="Sort", 
                                    fg="black",
                                    width=50, 
                                    command=self.click_timed_sorting_button)
        self.help_button = tk.Button(self.window, 
                                    text="Help!", 
                                    fg="black",
                                    width=50,
                                    command=self.show_message_box)
        
        # Place buttons
        self.add_to_list_button.grid(row=1, columnspan=3)
        self.help_button.grid(row=2, columnspan=3)
        self.start_timed_sorting.grid(row=5, columnspan=3)

        # Define Text Entry Box
        self.entry_0 = tk.Entry(self.window)

        # Place Text Entry Box
        self.entry_0.grid(row=0, column=1, columnspan=2)
        self.entry_0.focus()

    def show_message_box(self):
        messagebox.showinfo("How to enter the list", \
                            "Please enter the numbers one by one" + 
                            "as integers:\n" +
                            "e.g.: 1, -4, 3428.\n" + 
                            "All other characters are not allowed:\n" +
                            "e.g.: !$\%&dnyo.")


    # Define the lsit
    def add_to_list(self):
        """ Saves the user input in a list.
        """
        list_item = self.entry_0.get()
        try: 
            int(list_item)
            self.my_list.append(int(list_item))
        except:
            self.entry_0.delete(0, 'end')
        print(self.my_list)
        return self.my_list
    

    # Change label commands
    def set_my_unsorted_list_label(self):
        """ Dynamically changes the text of player_1_label to 
        update the winner count for player 1.
        """
        my_unsorted_list_label_text = "Unsorted list: " + str(self.my_list)
        return my_unsorted_list_label_text
    
    def set_my_sorted_list_label(self):
        """ Dynamically changes the text of player_1_label to 
        update the winner count for player 1.
        """
        self.my_sorted_list = self.sorting.sorting_alg(self.my_list)
        my_sorted_list_label_text = "Sorted list: " + str(self.my_sorted_list)
        return my_sorted_list_label_text
    
    # Button commands
    def click_add_to_list_button(self):
        self.add_to_list()
        self.entry_0.delete(0, 'end')
        self.label_1["text"] = self.set_my_unsorted_list_label()

    def click_timed_sorting_button(self):
        """ Calls the sorting algorithm (timed).
        """
        self.my_sorted_list = self.sorting.sorting_alg(self.my_list)
        self.label_2["text"] = self.set_my_sorted_list_label()

        

def main():
    root = tk.Tk()
    SelectionSortUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
