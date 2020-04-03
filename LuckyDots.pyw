import tkinter as tk
from tkinter import messagebox as msb
import tkinter.scrolledtext as scrolledtext
import os
import random as r

start = 4
border = 0
for x in os.listdir("data/files"):
	border += 1
last = border % 4
error = False
change_variable = False
back = False
choosen_list = []
end = False
ButtonActivate = False
upsentList = []
choice = None

def rgb(rgb):
	return "#%02x%02x%02x" % rgb


def EditGroup(name, window):
	if name != "":
		if name + '.txt' in [x for x in os.listdir('data/files')]:
			msb.askokcancel("Warning!", "For program to work propertly students must be written down following this"
										" pattern:\n\n[Number],[[Name] [Surname]\n[Number],[[Name] [Surname]\n\n[...]"
										"\n\nFor example:\n\n1,John Smith\n2,Daisy Williams\n\nNote! There is no "
										"spacebar between comma!")
			window.destroy()
			os.startfile("data\\files\\" + str(name) + '.txt')
			DataPage(root).GroupsText.config(state = 'normal')
		else:
			msb.showwarning("Error!", "This class is not in data base.")


def DeleteGroup(name, window):
	global change_variable
	if name != "":
		if str(name) + '.txt' in os.listdir('data/files'):
			MsgBox = msb.askokcancel("Warning!", "Are you sure that you want to delete classroom: "
									 + "''" + str(name) + "''?" )
			if MsgBox == True:
				window.destroy()
				change_variable = True

				os.remove("data\\files\\" + str(name) + '.txt')

				for x in os.listdir('data/files'):
					DataPage(root).GroupsText.insert(tk.END, "-->  " + x[:-4] + "\n")

				os.remove('data\\lottery files\\lottery_' + str(name) + '.txt')

				DataPage(root).GroupsText.config(state = 'normal')
				DataPage(root).GroupsText.delete('1.0', 'END')
		else:
			msb.showwarning("Error!", "This class is not in data base.")


def AddGroup(name, window):
	global change_variable
	if name != "":
		if name + '.txt' not in [x for x in os.listdir('data/files')]:
			MsgBox = msb.askokcancel("Warning!", "For program to work propertly students must be written down following"
												 " this pattern:\n\n[Number],[[Name] [Surname]\n[Number],[[Name]"
												 " [Surname]\n\n[...]\n\nFor example:\n\n1,John Smith\n2,Daisy Williams"
												 "\n\nNote! There is no spacebar between comma!")
			if MsgBox == True:
				window.destroy()
				change_variable = True
				try:
					f = open("data\\files\\"+ str(name) + '.txt', 'w+')
					os.startfile("data\\files\\" + str(name) + '.txt')

					for x in os.listdir('data/files'):
						DataPage(root).GroupsText.insert(tk.END, x[:-4] + '\n')

					DataPage(root).GroupsText.config(state = 'normal')
				except:
					pass
		else:
			msb.showwarning("Error!", "Class named this way already exists.")


def EditGroupWindow():
	global ButtonActivate
	window = tk.Tk()
	window.title("Window for editing class!")
	window.geometry('350x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol( "WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Give the name of a class,\nthat you want to edit:", font = ('Courier', 12))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Edit class", font = font, command = lambda: EditGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def DeleteGroupWindow():
	window = tk.Tk()
	window.title("Window for deleting class!")
	window.geometry('350x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol("WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Give the name of a class,\nthat you want to delete:", font = ('Courier', 12))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Delete class", font = font, command = lambda: DeleteGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def AddGroupWindow():
	window = tk.Tk()
	window.title("Window for adding class!")
	window.geometry('350x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol( "WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Give the name of a class,\nthat you want to add:", font = ('Courier', 12))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Add class", font = font, command = lambda: AddGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def NewWindow(new_window, frame):
	global start
	global error
	global back

	if back is False:
		start = 4
		error = False
		frame.destroy()
		window = new_window(root)
	else:
		msb.showwarning("Warning!", "Close this window before going back to menu.")


def Lottery(chancelabel, students, lenght, button, name, label, StudentCancel, UpsentButton):
	global choosen_list
	global choice
	global end
	global upsentList

	UpsentButton['state'] = 'normal'
	StudentCancel['state'] = 'normal'

	for student in upsentList:
		if student not in choosen_list:
			choosen_list.append(student)

	while True:
		if len(choosen_list) != lenght:
			choice = r.choice(students)
			end = False
			if choice not in choosen_list:
				break
			else:
				pass
		else:
			button['state'] = 'disabled'
			end = True
			label['text'] = 'Press to roll!'
			button['text'] = 'New queue!'
			msb.showinfo("That's it.", "End of the queue!")
			choice = None
			choosen_list = []
			open('data\\lottery files\\lottery_' + name, 'w').close()
			button['state'] = 'normal'
			chancelabel['text'] = 'Chance to roll a student: X%'
			break

	if end is False:
		button['text'] = 'Roll'
		try:
			var = str(choice).split(' ')
			label['text'] =	var[0] + '\n' + var[1] + '\n' + var[2]
			choosen_list.append(choice)
		except:
			pass
		try:
			chancelabel['text'] = \
				'Chance to roll a student: ' \
				+ str(int(round(1/(len(open('data\\files\\' + name).readlines()) - len(choosen_list)), 2)*100)) + '%'
		except:
			chancelabel['text'] = 'Chance to roll a student: ...%'
	else:
		pass


def upsent(UpsentButton):
	global choice
	global upsentList
	if choice is not None:
		if choice not in upsentList:
			upsentList.append(choice)

		msb.showinfo('Student upsent!', 'Rolled student had beed removed from the queue until closing this window')
		UpsentButton['state'] = 'disabled'
	else:
		msb.showerror('Error!', 'I couldnt find any student!')


def StudentCancelButton(StudentCancel):
	global choice
	global choosen_list
	if choice is not None:
		choosen_list.remove(choice)
		msb.showinfo('Undo!', "Rolled student had been canceled and put back to the queue at random position.")
		StudentCancel['state'] = 'disabled'
	else:
		msb.showerror('Error', "I couldn't find any student")


def LotteryWindow(name, d):
	global choosen_list
	global back
	students = []
	lenght = 0

	for x in open('data\\files\\' + name, 'r'):
		students.append(x.strip().replace(',', ' '))
		lenght += 1

	back = True
	try:
		for x in open('data\\lottery files\\lottery_' + name, 'r'):
			choosen_list.append(''.join(x.strip().split(',')))
	except:
		f = open('data\\lottery files\\lottery_' + name, 'w+')

	def Exit():
		global choosen_list
		global back
		global upsentList

		upsentList = []

		open('data\\lottery files\\lottery_' + name, 'w').close()
		f = open('data\\lottery files\\lottery_' + name, 'a')
		txt = ''

		for x in choosen_list:
			for y in x:
				txt += y
			txt += '\n'
		f.write(txt)
		choosen_list = []
		back = False
		try:
			for x in d:
				d[x].config(state = 'normal')
		except:
			pass
		window.destroy()

	window = tk.Tk()
	window.geometry('500x400')
	window.attributes("-topmost", True)
	window.protocol( "WM_DELETE_WINDOW", Exit)
	window.title(name[:-4])
	window.resizable(False, False)
	window.title('Lottery!')

	for x in d:
		d[x].config(state = 'disabled')

	frame = tk.Frame(window, bg = 'grey')
	frame.place(relwidth = 1, relheight = 1)

	ChanceLabel = tk.Label(window, text = "Chance to roll a student: X%", font = ('Courier', 16), bg = 'grey',
						   anchor = 'w', fg = 'white')
	ChanceLabel.place(relx = 0.05, rely = 0.9, relwidth = 1, relheight = 0.1)

	try:
		ChanceLabel['text'] = 'Chance to roll a student: '\
							  +str(int(round(1/(len(open('data\\files\\'
														 +name).readlines()) - len(choosen_list)), 2)*100)) + '%'
	except:
		ChanceLabel['text'] = 'Chance to roll a student: X%'

	DisplayLabel = tk.Label(window, text = "Press to roll!", font = ('Courier', 25), fg = 'white',
							bg = 'grey', anchor = 'center')
	DisplayLabel.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.4)

	StudentCancel = tk.Button(frame, text = 'Undo', font = ('Courier', 15),
							  command = lambda: StudentCancelButton(StudentCancel))
	StudentCancel.place(relx = 0.15, rely = 0.75, relwidth = 0.3, relheight = 0.15)

	Upsent = tk.Button(frame, text = "Upsent", font = ('Courier', 15), command = lambda: upsent(Upsent))
	Upsent.place(relx = 0.55, rely = 0.75, relwidth = 0.3, relheight = 0.15)

	ActionButton = tk.Button(frame, text = "Roll", font = font,
							 command = lambda: Lottery(ChanceLabel,students, lenght, ActionButton, name,
													   DisplayLabel, StudentCancel, Upsent))
	ActionButton.place(relx = 0.15, rely = 0.50, relwidth = 0.7, relheight = 0.2)

	window.mainloop()


class StartPage:
	def __init__(self, master):

		frame = tk.Frame(master, bg = 'grey')
		frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

		self.LotteryButton = tk.Button(frame, text = 'Lottery', font = font,
									   command = lambda: NewWindow(LotteryPage, frame))
		self.LotteryButton.place(relx = 0.25, rely = 0.25, relwidth = 0.5, relheight = 0.15)

		self.EditButton = tk.Button(frame, text = "Data Base", font = font,
									command = lambda: NewWindow(DataPage, frame))
		self.EditButton.place(relx = 0.25, rely = 0.45, relwidth = 0.5, relheight = 0.15)

		self.QuitButton = tk.Button(frame, text = 'Exit', font = font, command = lambda: root.destroy())
		self.QuitButton.place(relx = 0.25, rely = 0.65, relwidth = 0.5, relheight = 0.15)

		self.MyOwnLabel = tk.Label(frame, text = "Szymon Molęda\n2020", font = ('Courier', 15),
								   bg = 'grey', foreground = 'white')
		self.MyOwnLabel.place(relx = 0.35, rely = 0.88, relwidth = 0.3, relheight = 0.1)

		self.TitleLabel = tk.Label(frame, text = 'Lucky\nDots', font = ('Courier', 30),
								   bg = 'grey', foreground = 'white')
		self.TitleLabel.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.15)


class LotteryPage:
	global change_variable

	def __init__(self, master):
		global start

		if change_variable is False:

			frame = tk.Frame(master, bg = 'grey')
			frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

			self.LotteryFrame = tk.Label(frame, bg = 'grey')
			self.LotteryFrame.place(relx = 0.1, rely = 0.15, relwidth = 0.8, relheight = 0.7)

			d = {}
			for name in enumerate(os.listdir('data/files')):
				d['button{}'.format(name[0])] = tk.Button(self.LotteryFrame, text = str(name[1][:-4]), height = 3,
														  width = 30, font = ('Courier', 16),
														  command = lambda name = name[1]: LotteryWindow(name, d))

			try:
				for x in range(start):
					d['button{}'.format(x)].pack(pady = 6)
			except:
				pass

			self.label = tk.Label(frame, text = 'Choose class', font = ('Courier', 30), bg = 'grey', fg = 'white')
			self.label.place(relx = 0.14, rely = 0.03, relwidth = 0.72, relheight = 0.1)

			self.NextButton = tk.Button(frame, text = "---->", font = ('Courier', 16),
										command = lambda: NextPage(d, self.NextButton))
			self.NextButton.place(rely = 0.875, relx = 0.7, relwidth = 0.2, relheight = 0.1)

			self.PreviousButton = tk.Button(frame, text = "<----", font = ('Courier', 16),
											command = lambda: PreviousPage(d, self.NextButton))
			self.PreviousButton.place(rely = 0.875, relx = 0.1, relwidth = 0.2, relheight = 0.1)

			if len(d) <= 4:
				self.NextButton.config(state = 'disabled')
				self.PreviousButton.config(state = 'disabled')

			self.BackButton = tk.Button(frame, text = "Back",
										command = lambda: NewWindow(StartPage, frame), font = font)
			self.BackButton.place(rely = 0.875, relx = 0.35,relwidth = 0.3, relheight = 0.1)

		else:
			global window
			window = StartPage(root)
			msb.showwarning("Error!", "You have done changes to the data base, restart is required.")

		def NextPage(d, button):
			global start
			global error
			global last
			global border

			try:
				for x in range(start):
					d['button{}'.format(x)].pack_forget()
				for x in range(start, start + 4):
					d['button{}'.format(x)].pack(pady = 6)
				if border % 4 == 0:
					button['state'] = 'disabled'
			except:
				error = True
				start = start - 4
			start = start + 4

		def PreviousPage(d, button):
			global start
			global last
			global error
			button['state'] = 'normal'
			if start >= 4:
				if error == False:
					for x in range(start):
						d['button{}'.format(x)].pack_forget()
					try:
						for x in range(start - 8, start - 4):
							d['button{}'.format(x)].pack(pady = 6)
					except:
						for x in range(start):
							d['button{}'.format(x)].pack(pady = 6)
						start += 4
				else:
					for x in range(border - 1, border - last - 1, -1):
						d['button{}'.format(x)].pack_forget()
					for x in range(start - 4, start):
						d['button{}'.format(x)].pack(pady = 6)
					start = start + 4
					error = False
				start = start - 4


class DataPage:
	def __init__(self, master):

		frame = tk.Frame(master, bg = 'grey')
		frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

		self.GroupsText = scrolledtext.ScrolledText(frame, bg = 'white', font = ('Courier', 16))
		self.GroupsText.place(relx = 0.3, rely = 0.05, relwidth = 0.6, relheight = 0.8)

		self.AddGroupButton = tk.Button(frame, text = "Add class", font = ('Courier', 10),
										command = lambda: AddGroupWindow())
		self.AddGroupButton.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.1)

		self.DeleteButton = tk.Button(frame, text = "Delete class", font = ('Courier', 10),
									  command = lambda:	DeleteGroupWindow())
		self.DeleteButton.place(relx = 0.05, rely = 0.3, relwidth = 0.2, relheight = 0.1)

		self.GroupsText.insert(tk.END, 'Classes in data base:\n\n', ('p'))
		self.GroupsText.tag_add('p', '1.0', '1.0')
		self.GroupsText.tag_config('p', font = ('Courier', 18))

		for x in os.listdir('data/files'):
			self.GroupsText.insert(tk.END, "-->  " + x[:-4] + "\n")

		self.GroupsText.config(state="disabled")

		self.EditGroupButton = tk.Button(frame, text = 'Edit class', font = ('Courier', 10),
										 command = lambda: EditGroupWindow())
		self.EditGroupButton.place(relx = 0.05, rely = 0.55, relwidth = 0.2, relheight = 0.1)

		self.BackButton = tk.Button(frame, text = "Back", font = font,
									command = lambda: NewWindow(StartPage, frame))
		self.BackButton.place(rely = 0.875, relx = 0.1, relwidth = 0.8, relheight = 0.1)


root = tk.Tk()
root.geometry('800x800')
root.title('Lucky Dots')
font = ('Courier', 20)
root.resizable(False, False)

background_image = tk.PhotoImage(file ='data/background/bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relheight = 1, relwidth = 1)

window = StartPage(root)
root.mainloop()
