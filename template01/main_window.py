'''

this code amended from the repository on GitHub: https://github.com/Rickiarty/PDF_editor

'''

from window import Window

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import simpledialog as s_dialog

class MainWindow(Window):
    # widgets
    _window               = None
    _button1         = None

    def initialize(self):
        # construct an object of window
        self._window = tk.Tk()
        # set title, size, position, event(s), and background color of window
        self._window.title('some desktop app - v{} © 2022 {}'.format(self.version, self.author))
        width = 1000
        height = 600
        position_x = int(self._window.winfo_screenwidth()/2 - width/2)
        position_y = int(self._window.winfo_screenheight()/2 - height/2)
        self._window.geometry('{}x{}'.format(width, height)) # size: width x height
        self._window.geometry('+{}+{}'.format(position_x, position_y)) # position of left-top of window
        self._window.configure(background='gray') # background color
        self._window.protocol(name="WM_DELETE_WINDOW", func=self._on_closing) # set event handler on closing window

        # build buttons
        self._merge_button = tk.Button(self._window, 
                                        width = 64, 
                                        height=2, 
                                        text='Button 1', 
                                        command=self._button1_pressed, 
                                        relief=tk.RIDGE, 
                                        borderwidth=5)
        self._merge_button.pack()
    
    def _on_closing(self):
        if mb.askokcancel("Quit", "Do you want to quit?"):
            self._window.destroy()
    
    def run(self):
        # run app
        self._window.mainloop()

    def _button1_pressed(self): # event method/function after button 1 is pressed 
        reply = mb.askokcancel("Hello", "How are you today?")
        print('result from dialogue: %s' % reply)
