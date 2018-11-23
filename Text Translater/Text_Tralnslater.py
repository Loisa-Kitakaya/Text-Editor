# Author Loisa Kitakaya

# This is a program that will translate text from one language to another.
# The program is written in python3.
# It will use the following modules/libraries: Python-Microsoft-Translate-API | Goslate: Free Google Translate API | Tkinter
# The program will work mainly with english to french and vice versa.

import tkinter
import goslate
from tkinter import *
import tkinter.messagebox
from mstranslate import MSTranslate
import tkinter.filedialog as fdialog

# gs = goslate.Goslate()
# translatedText = gs.translate(text,'fr')

# kk = MSTranslate('client_id', 'client_secret')
# print(kk.translate('你好', 'en'))

# creating a class to define window (GUI) properties
class GUI_Window:

	# creating constructor to initialize window (GUI) creation
	def __init__(self, master):

		# naming the window 
		master.title("Text Translater")

		# setting the size of the window
		# master.geometry("800x500")

		# creating the menu bar
		menu_bar = Menu(master)
		master.config(menu = menu_bar)

		# creating sub-menu "Options"
		sub_menu_1 = Menu(menu_bar)
		menu_bar.add_cascade(label = "Options", menu = sub_menu_1)
		# creating sub-menu "Options" commands'
		sub_menu_1.add_command(label = "Open file", command = self.open_file)
		sub_menu_1.add_command(label = "Quit app", command = master.destroy)

		# creating sub-menu "About"
		sub_menu_2 = Menu(menu_bar)
		menu_bar.add_cascade(label = "info", menu = sub_menu_2)
		# creating sub-menu "About" commands'
		sub_menu_2.add_command(label = "About", command = self.about)

		# creating the main frame frame
		frame_1 = Frame(master)

		# displaying the frame
		frame_1.pack(fill = "both", expand = 1)

		# creating sub-frames
		frame_001 = Frame(frame_1)
		frame_101 = Frame(frame_1)
		frame_102 = Frame(frame_1)
		frame_002 = Frame(frame_1)
		frame_103 = Frame(frame_1)

		# displaying the sub-frames
		frame_001.pack(side = TOP, fill = "both", padx=5)
		frame_101.pack(fill = "both", expand = 1, padx=5, pady=5)
		frame_102.pack(padx=5,)
		frame_002.pack(fill = "both", padx=5)
		frame_103.pack(fill = "both", expand = 1, padx=5, pady=5)

		# creating labels for the language sections
		label_1 = Label(frame_001, text = "English")
		label_2 = Label(frame_002, text = "French")

		# displaying the labels
		label_1.pack(side = LEFT)
		label_2.pack(side = LEFT)

		# creating entry fields
		text_box_1 = Text(frame_101, bg = "white", height = 15)
		text_box_2 = Text(frame_103, bg = "white", height = 15)

		# displaying the entry fields
		text_box_1.pack()
		text_box_2.pack()

		# creating the translate and clear buttons
		button_1 = Button(frame_102, text = "Translate")
		button_2 = Button(frame_102, text = "Clear")

		# displaying the buttons
		button_1.pack(side = RIGHT, padx= 5)
		button_2.pack(side = RIGHT, padx = 5)

		# creating the status bar
		status_bar = Label(master, text = "Version 1.0", bd = 1, relief = SUNKEN, anchor = W)

		# displaying the status bar
		status_bar.pack(side = BOTTOM, fill = "x")

	# defining the commands for the menu bar

	# commands for "Open file"
	def open_file(self):

		# using fdialog
		global file_to_open

		self.file_to_open = fdialog.askopenfilename(initialdir = "/home", title = "Open a text file", filetypes = (("text files", "*.txt"),("all files","*.*")))

	# commands for "About"
	def about(self):

		# using messagebox
		tkinter.messagebox.showinfo("About Text Translater 1.0", "*********** ABOUT *********** \n\nText Translater 1.0 is a software that translates your test from one human language to another e.g. eng --> fr \n\n********** AUTHOR ********** \n\nFreedom Loisa Kitakaya")

GUI =Tk()

main_window = GUI_Window(GUI)

icon = Image("photo", file="icon.png")
GUI.tk.call('wm','iconphoto',GUI._w, icon)
GUI.mainloop()