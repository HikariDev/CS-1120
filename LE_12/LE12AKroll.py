# Name: Andrew Kroll
# Date: 2020-12-10
# Course-Section/LE#: CS1120-951 LE12
# Description: tkinter, sorting, and searching

import tkinter
import tkinter.messagebox
import random


class UserInterface:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("480x130")

        self.num_list = [random.randint(0, 100) for i in range(10)]

        self.options_frame = tkinter.Frame(self.main_window)
        self.entry_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.num_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.options_frame, text='Search',
                                       variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.options_frame, text='Sort',
                                       variable=self.radio_var, value=2)

        self.rb1.pack(side='left')
        self.rb2.pack(side='left')

        self.prompt_lbl = tkinter.Label(self.entry_frame,
                                        text='Enter a number to search for:')
        self.search_box = tkinter.Entry(self.entry_frame, width=10)
        self.result_var = tkinter.StringVar()
        self.result_lbl = tkinter.Label(self.entry_frame,
                                        text='Index of search value:')
        self.result_txt = tkinter.Label(self.entry_frame,
                                        textvariable=self.result_var)
        self.sorted_list = tkinter.StringVar()
        self.sort_lbl = tkinter.Label(self.num_frame,
                                      text='Sorted list:')
        self.sort_txt = tkinter.Label(self.num_frame,
                                      textvariable=self.sorted_list)

        self.prompt_lbl.pack(side='left')
        self.search_box.pack(side='left')
        self.result_lbl.pack(side='left')
        self.result_txt.pack(side='left')
        self.sort_lbl.pack(side='left')
        self.sort_txt.pack(side='left')

        self.search_button = tkinter.Button(self.button_frame,
                                            text='Search',
                                            command=self.process,
                                            bg='#f0a0a0')
        self.sort_button = tkinter.Button(self.button_frame,
                                          text='Sort',
                                          command=self.process,
                                          bg='#a0f0a0')
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy,
                                          bg='#a0a0f0')

        self.search_button.pack(side='left', padx=5)
        self.sort_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        self.options_frame.pack(pady=4)
        self.entry_frame.pack(pady=4)
        self.button_frame.pack(pady=4)
        self.num_frame.pack(pady=10)

        tkinter.mainloop()

    def process(self):
        option = self.radio_var.get()
        if option == 0:
            tkinter.messagebox.showinfo('Error!', 'You must select one of the '
                                                  'options (Search or Sort)!')
        elif option == 1:
            if self.search_box.get() == '':
                tkinter.messagebox.showinfo('Error!', 'You must enter a '
                                                      'value to search for!')
                return
            target = float(self.search_box.get())
            target_index = self.linear_search(target)
            self.result_var.set(target_index)
        else:
            self.insertion_sort()
            display_list = ""
            for num in self.num_list:
                if display_list != "":
                    display_list += ", "
                display_list += str(num)
            self.sorted_list.set(display_list)

    def linear_search(self, num):
        for i in range(len(self.num_list)):
            if num == self.num_list[i]:
                return i
        return -1

    def insertion_sort(self):
        for i in range(1, len(self.num_list)):
            item = self.num_list[i]
            j = i - 1
            while j >= 0 and self.num_list[j] > item:
                self.num_list[j+1] = self.num_list[j]
                j -= 1
            self.num_list[j + 1] = item



user_interface = UserInterface()
