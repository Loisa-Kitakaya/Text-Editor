# Author Loisa Kitakaya

# This is a program that will translate text from one language to another.
# The program is written in python3.
# It will use the following modules/libraries: IBM Watson™ Language Translator | Tkinter
# The program will work mainly with english to french and vice versa.

import os
import json
import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog as fdialog
import tkinter.scrolledtext as scrolltextbox
from watson_developer_cloud import LanguageTranslatorV3

# token-based Identity and Access Management (IAM) authentication
language_translator = LanguageTranslatorV3(

    version='2018-05-01',
    iam_apikey='-6-QG-NTBvcMI9RMbKPCHaFpXg4lKbQ9pQfq-BNSAprq',
    url='https://gateway-wdc.watsonplatform.net/language-translator/api'

)

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
		sub_menu_1.add_command(label = "Edit file", command = self.open_file)
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
		label_1 = Label(frame_001, text = "Input")
		label_2 = Label(frame_002, text = "Output")

		# displaying the labels
		label_1.pack(side = LEFT)
		label_2.pack(side = LEFT)

		# creating entry fields
		text_box_1 = scrolltextbox.ScrolledText(frame_101, bg = "white", height = 15, wrap = WORD, relief=SUNKEN)
		text_box_2 = scrolltextbox.ScrolledText(frame_103, bg = "white", height = 15, wrap = WORD, relief=SUNKEN)

		# displaying the entry fields
		text_box_1.pack(fill = "both")
		text_box_2.pack(fill = "both")

		# defining the commands for the buttons

		# command for the clear button
		def clear():

			# clearing the text box
			text_box_1.delete('1.0', END)

		# command for the clear all button
		def clear_all():

			# clearing all the text boxes
			text_box_1.delete('1.0', END)
			text_box_2.delete('1.0', END)

		# command to get, translate and display text
		def translate():

			# getting the text
			source_lang = text_box_1.get('1.0', END)

			# translating the text

			# checking if text box is empty or not: to determine if translation will take place
			if len(text_box_1.get("1.0", "end-1c")) == 0:

				tkinter.messagebox.showwarning("No input!", "Please provide text to be translated in the top text box.")

			else:

				while True:

					# selecting the kind of language translation
					lang = tkinter.simpledialog.askinteger("Select output language", "How do you want your translation? \n[1: English to French] \n[2: French to English]")

					if lang == 1:

						# english to french translation
						translation = language_translator.translate(source_lang, model_id='en-fr').get_result()
						translated_text = json.dumps(translation, indent=2, ensure_ascii=False)

						# displaying the output
						text_box_2.insert('1.0', "\n*******************************************************************************")

						text_box_2.insert('1.0', "\n", translated_text)

						text_box_2.insert('1.0', translated_text)

						text_box_2.insert('1.0', "\n", translated_text)

						text_box_2.insert('1.0', "\n*******************************************************************************")

						break

					elif lang == 2:

						# french to english translation
						translation = language_translator.translate(source_lang, model_id='fr-en').get_result()
						translated_text = json.dumps(translation, indent=2, ensure_ascii=False)

						# displaying the output
						text_box_2.insert('1.0', "\n*******************************************************************************")

						text_box_2.insert('1.0', "\n", translated_text)

						text_box_2.insert('1.0', translated_text)

						text_box_2.insert('1.0', "\n", translated_text)

						text_box_2.insert('1.0', "\n*******************************************************************************")

						break

					else:

						# warning to select correct/provided options
						tkinter.messagebox.showwarning("Warning", "Please select the provided options, Other language translations will be available in future versions of Text Translator.")

						continue

		# command to browse for file to load
		def browse():

			# using fdialog
			global file_to_open

			# openig dialog box to open text file
			self.file_to_open = fdialog.askopenfilename(initialdir = "/home", title = "Open to translate a text file", filetypes = (("text files", "*.txt"),("all files","*.*")))

			# loading and displaying the file and it's content to text box 1

			open_f = open(self.file_to_open, "r")
			read_f = open_f.read()

			text_box_1.insert('1.0', read_f)

		# creating the translate and clear buttons
		button_1 = Button(frame_102, text = "Translate", relief = RAISED, command = translate)
		button_2 = Button(frame_102, text = "Clear", relief = RAISED, command = clear)
		button_3 = Button(frame_102, text = "Clear All", relief = RAISED, command = clear_all)
		button_4 = Button(frame_102, text = "Browse", relief = RAISED, command = browse)

		# displaying the buttons
		button_4.pack(side = RIGHT, padx = 5)
		button_1.pack(side = RIGHT, padx = 5)		
		button_3.pack(side = RIGHT, padx = 5)
		button_2.pack(side = RIGHT, padx = 5)

		# creating the status bar
		status_bar = Frame(master)
		status = Label(status_bar, text = "Version 1.0", bd = 1, relief = SUNKEN, anchor = E)

		# displaying the status bar
		status_bar.pack(side = BOTTOM, fill = "x", padx = 5)
		status.pack(side = BOTTOM, fill = "x")

	# defining the commands for the menu bar

	# commands for "Open file"
	def open_file(self):

		# using fdialog
		global file_to_open

		# openig dialog box to open text file
		self.file_to_open = fdialog.askopenfilename(initialdir = "/home", title = "Open to edit a text file", filetypes = (("text files", "*.txt"),("all files","*.*")))

		# loading and displaying the file and it's content to text box 1
		os.system("gvim " + self.file_to_open)

	# commands for "About"
	def about(self):

		# using messagebox
		tkinter.messagebox.showinfo("About Text Translater 1.0", "*********** ABOUT *********** \n\nText Translater 1.0 is a software that translates your test from one human language to another e.g. en --to--> fr \n\n********** AUTHOR ********** \n\nFreedom Loisa Kitakaya")

GUI =Tk()

main_window = GUI_Window(GUI)

icon = Image("photo", file="icon.png")
GUI.tk.call('wm','iconphoto',GUI._w, icon)
GUI.mainloop()